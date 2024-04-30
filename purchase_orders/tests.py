from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Vendor, HistoricalPerformance
from purchase_orders.models import PurchaseOrder
from vendor_profiles.serializers import VendorSerializer
from purchase_orders.serializers import PurchaseOrderSerializer
from django.contrib.auth.models import User


class PurchaseOrderTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="testvendor",
            contact_details="testcontactdetails",
            address = "testaddress",
            vendor_code = "testvendorcode",
        )
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="1234567890",
            vendor=self.vendor,
            order_date="2021-01-01",
            delivery_date="2021-01-02",
            status="completed",
            quality_rating=5,
            acknowledgment_date="2021-01-01",
        )

    def test_create_purchase_order(self):
        """
        Ensure we can create a new purchase order object.
        """
        url = reverse("purchase_order_list_create")
        data = {
            "po_number": "1234567891",
            "vendor": self.vendor.id,
            "order_date": "2021-01-01",
            "delivery_date": "2021-01-02",
            "status": "completed",
            "quality_rating": 5,
            "acknowledgment_date": "2021-01-01",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)
        self.assertEqual(PurchaseOrder.objects.filter(vendor=self.vendor).last().po_number, "1234567891")

    def test_get_purchase_order(self):
        """
        Ensure we can get a purchase order object.
        """
        url = reverse("purchase_order_retrieve_update_destroy", args=[self.purchase_order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["po_number"], "1234567890")

    def test_update_purchase_order(self):
        """
        Ensure we can update a purchase order object.
        """
        url = reverse("purchase_order_retrieve_update_destroy", args=[self.purchase_order.id])
        data = {
            "po_number": "1234567891",
            "vendor": self.vendor.id,
            "order_date": "2021-01-01",
            "delivery_date": "2021-01-02",
            "status": "completed",
            "quality_rating": 5,
            "acknowledgment_date": "2021-01-01",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(PurchaseOrder.objects.all())
        self.assertEqual(PurchaseOrder.objects.get(vendor=self.vendor).po_number, "1234567891")

    def test_delete_purchase_order(self):
        """
        Ensure we can delete a purchase order object.
        """
        url = reverse("purchase_order_retrieve_update_destroy", args=[self.purchase_order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

