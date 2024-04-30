from django.urls import path
from .api_views import (PurchaseOrderListCreateAPIView,
                        PurchaseOrderRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('', PurchaseOrderListCreateAPIView.as_view(), name = "purchase_order_list_create"),
    path('<int:id>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name = "purchase_order_retrieve_update_destroy"),
]