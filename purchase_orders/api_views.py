from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PurchaseOrderSerializer
from .models import PurchaseOrder
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class PurchaseOrderListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()


class PurchaseOrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()
    lookup_field = "id"
