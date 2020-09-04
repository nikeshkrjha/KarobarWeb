from django.shortcuts import render
from api.serializers import CustomerSerializer, SuppliersSerializer, PaymentsReceivedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from karobar.models import Customer, Supplier, Purchase, SupplierPayment, PaymentsReceived
from decimal import Decimal

# Create your views here.


class CustomerList(APIView):
    """
    List all customers, or create a new snippet.
    """

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        data = {'data': serializer.data}
        return Response(data)


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
