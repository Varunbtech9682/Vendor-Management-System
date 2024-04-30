from django.urls import path
from .api_views import (VendorListCreateAPIView,
                        VendorRetrieveUpdateDestroyAPIView,
                        VendorPermanceEvaluationAPIView)

urlpatterns = [
    path('', VendorListCreateAPIView.as_view(), name="vendor_list_create"),
    path('<int:id>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name="vendor_retrieve_update_destroy"),
    path('<int:id>/performance/', VendorPermanceEvaluationAPIView.as_view(), name="historical_performance")
]
