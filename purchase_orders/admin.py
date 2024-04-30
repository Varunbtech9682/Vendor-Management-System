from django.contrib import admin
from .models import (PurchaseOrder)

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date')
    list_filter = ('status', 'vendor', 'order_date', 'delivery_date')
    search_fields = ('po_number', 'vendor', 'order_date', 'delivery_date', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date')
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
