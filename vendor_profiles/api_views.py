from .models import Vendor, HistoricalPerformance
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,)
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VendorSerializer, HistoricalPerformanceSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="id",
            description="Vendor ID",
            required=True,
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
        )
    ],
    examples=[
        OpenApiExample(
            name="Vendor 1",
            value={
                "id": 1,
                "name": "Vendor 1",
                "address": "123 Main St",
                "city": "Austin",
                "state": "TX",
                "zip_code": "78701",
                "country": "USA",
                "phone_number": "512-555-5555",
                "email": "test@gmail.com",
                "contact_name": "John Doe",
                "on_time_delivery_rate": 0.95,
                "quality_rating_avg": 0.95,
                "average_response_time": 1.5,
                "fulfillment_rate": 0.95,
            },
        ),
        OpenApiExample(
            name="Vendor 2",
            value={
                "id": 2,
                "name": "Vendor 2",
                "address": "123 Main St",
                "city": "Austin",
                "state": "TX",
                "zip_code": "78701",
                "country": "USA",
                "phone_number": "512-555-5555",
                "email": "test@gmail.com",
                "contact_name": "Jane Doe",
                "on_time_delivery_rate": 0.95,
                "quality_rating_avg": 0.95,
                "average_response_time": 1.5,
                "fulfillment_rate": 0.95,
            },
        ),
    ],
)

class VendorListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="id",
            description="Vendor ID",
            required=True,
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
        )
    ],
    examples=[
        OpenApiExample(
            name="Vendor 1",
            value={
                "id": 1,
                "name": "Vendor 1",
                "address": "123 Main St",
                "city": "Austin",
                "state": "TX",
                "zip_code": "78701",
                "country": "USA",
                "phone_number": "512-555-5555",
                "email": "testemail@gmail.com",
                "contact_name": "John Doe",
                "on_time_delivery_rate": 0.95,
                "quality_rating_avg": 0.95,
                "average_response_time": 1.5,
                "fulfillment_rate": 0.95,
            },
        ),
        OpenApiExample(
            name="Vendor 2",
            value={
                "id": 2,
                "name": "Vendor 2",
                "address": "123 Main St",
                "city": "Austin",
                "state": "TX",
                "zip_code": "78701",
                "country": "USA",
                "phone_number": "512-555-5555",
                "email": "test@gmail.com",
                "contact_name": "Jane Doe",
                "on_time_delivery_rate": 0.95,
                "quality_rating_avg": 0.95,
                "average_response_time": 1.5,
                "fulfillment_rate": 0.95,
            },
        ),
    ],
)



class VendorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="id",
            description="Historical Performance",
            required=True,
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
        )
    ],
    examples=[
        OpenApiExample(
            name="Vendor 1",
            value={
                "id": 1,
                "name": "Vendor 1",
                "address": "123 Main St",
                "city": "Austin",
                "state": "TX",
                "zip_code": "78701",
                "country": "USA",
                "phone_number": "512-555-5555",
                "email": "test1@gmail.com",
                "contact_name": "John Doe",
                "on_time_delivery_rate": 0.95,
                "quality_rating_avg": 0.95,
                "average_response_time": 1.5,
                "fulfillment_rate": 0.95,
            },
        ),
        OpenApiExample(
            name="Vendor 2",
            value={
                "id": 2,
                "name": "Vendor 2",
                "address": "123 Main St",
                "city": "Austin",
                "state": "TX",
                "zip_code": "78701",
                "country": "USA",
                "phone_number": "512-555-5555",
                "email": "test2@gmail.com",
                "contact_name": "Jane Doe",
                "on_time_delivery_rate": 0.95,
                "quality_rating_avg": 0.95,
                "average_response_time": 1.5,
                "fulfillment_rate": 0.95,
            },
        ),
    ],
)

class VendorPermanceEvaluationAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    
    def get(self, request, id, *args, **kwargs):
        metrics = HistoricalPerformance.objects.filter(vendor=id)
        metrics = HistoricalPerformanceSerializer(metrics, many=True).data

        return Response({'metrics': metrics})


