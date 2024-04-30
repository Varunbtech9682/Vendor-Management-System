from rest_framework.serializers import ModelSerializer
from .models import Vendor, HistoricalPerformance


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class HistoricalPerformanceSerializer(ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'