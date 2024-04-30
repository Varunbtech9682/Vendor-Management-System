from rest_framework.serializers import Serializer, ModelSerializer
from .models import PurchaseOrder


class PurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
    
    def create(self, validated_data):
        po = PurchaseOrder.objects.create(**validated_data)
        po.save()
        return po