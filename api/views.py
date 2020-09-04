from django.shortcuts import render
from api.serializers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from karobar.models import Customer, Supplier, Purchase, SupplierPayment, PaymentsReceived

# Create your views here.


class CustomerList(APIView):
    """
    List all customers, or create a new snippet.
    """

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        print(customers)
        data = {'data': serializer.data}
        return Response(data)
