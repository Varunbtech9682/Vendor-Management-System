from django.db import models
from vendor_profiles.models import Vendor
from django.db.models import signals
from vendor_profiles.models import Vendor, HistoricalPerformance
from django.db.models import Avg
from django.utils.timezone import now


STATUS = (
    ("pending", "pending"),
    ("completed", "completed"),
    ("canceled", "canceled"),
)

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=10)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=now)
    delivery_date = models.DateTimeField()
    items = models.JSONField(default=dict)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=100)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
def historical_performance_handler(sender, instance, **kwargs):
    # print("Called Historical Performance Handler!!!!")
    # print("Instance Vendor:  ",instance.vendor)
    po_status_completed = instance.status=="completed"
    po_status_changed = (instance.status=="completed")or(instance.status=="canceled")
    po_quality_rating = instance.quality_rating
    po_acknowledged = instance.acknowledgment_date
    po_count = 0
    completed_po = 0

    po = PurchaseOrder.objects.filter(vendor=instance.vendor)

    if po_status_completed:
        po = po.filter(status="completed")
        for po_item in po:
            if po_item.order_date <= po_item.delivery_date:
                po_count += 1
            if po_item.status == 'completed':
                completed_po += 1
        if completed_po == 0 or po_count == 0:
            on_time_delivery_rate = 0
        else:
            on_time_delivery_rate = po_count/completed_po

    if po_quality_rating:
        quality_rating_avg = po.aggregate(Avg('quality_rating'))
        quality_rating_avg = quality_rating_avg['quality_rating__avg']

    if po_acknowledged:
        avg_response_time = 0
        for po_item in po:
            date_diff = po_item.delivery_date - po_item.acknowledgment_date
            if date_diff.days < 0:
                date_diff = 0
            # print(f"PO: {po_item.po_number} ,Date_Diff: {int(date_diff.days)}, Ack_Date: {po_item.acknowledgment_date}, Del_Date: {po_item.delivery_date}")
            avg_response_time += int(date_diff.days)
        po_count = po.count()
        if po_count == 0 or avg_response_time == 0:
            avg_response_time = 0
        else:
            avg_response_time = avg_response_time/po_count

    fulfilment_rate = 0
    if po_status_changed:
        completed_po = po.filter(status="completed").count()
        all_po = po.count()
        if all_po == 0 or completed_po == 0:
            fulfilment_rate = 0
        else:
            fulfilment_rate = completed_po/all_po

    hp = HistoricalPerformance.objects.create(
        vendor=instance.vendor,
        on_time_delivery_rate = on_time_delivery_rate,
        quality_rating_avg = quality_rating_avg,
        average_response_time = avg_response_time,
        fulfillment_rate = fulfilment_rate,
    )
    hp.save()
    # po_dict = {
    #     "vendor":instance.vendor,
    #     "on_time_delivery_rate" : on_time_delivery_rate,
    #     "quality_rating_avg" : quality_rating_avg,
    #     "average_response_time" : avg_response_time,
    #     "fulfillment_rate" : fulfilment_rate,
    # }
    # print(po_dict)

signals.post_save.connect(historical_performance_handler, sender=PurchaseOrder)
