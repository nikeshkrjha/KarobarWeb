from rest_framework import serializers
from karobar.models import Customer, Supplier, SupplierPayment, PaymentsReceived, Sales, Purchase


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'customer_fname', 'customer_lname', 'email',
                  'phone_number', 'customer_city', 'customer_zipcode')


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'supplier_name', 'email',
                  'phone_number', 'supplier_city', 'supplier_zipcode')


class PaymentsReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsReceived
        fields = ('id', 'description', 'amount',
                  'payment_date', 'paid_by')
