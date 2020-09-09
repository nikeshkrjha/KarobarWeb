from django.shortcuts import render
from api.serializers import CustomerSerializer, SuppliersSerializer, PaymentsReceivedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from karobar.models import Customer, Supplier, Purchase, SupplierPayment, PaymentsReceived
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

# ============ OLD IMPLEMENTATION =============== #

# class CustomerList(APIView):
#     """
#     List all customers, or create a new snippet.
#     """

#     def get(self, request, format=None):
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         data = {'data': serializer.data}
#         return Response(data)
# ============ OLD IMPLEMENTATION =============== #

# ============ NEW IMPLEMENTATION USING MIXINS =============== #


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
# ============ NEW IMPLEMENTATION USING MIXINS =============== #


class SupplierList(APIView):
    """
    List all customers, or create a new snippet.
    """

    def get(self, request, format=None):
        suppliers = Supplier.objects.all()
        serializer = SuppliersSerializer(suppliers, many=True)
        data = {'data': serializer.data}
        return Response(data)


class PaymentsReceivedList(APIView):
    """
    List all customers, or create a new snippet.
    """

    def get(self, request, format=None):
        paymentsList = PaymentsReceived.objects.all()
        serializer = PaymentsReceivedSerializer(paymentsList, many=True)
        data = {'data': serializer.data}
        return Response(data)
