from rest_framework import serializers
from karobar.models import Customer, Supplier, SupplierPayment, PaymentsReceived, Sales, Purchase


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_fname', 'customer_lname', 'email',
                  'phone_number', 'customer_city', 'customer_zipcode')
