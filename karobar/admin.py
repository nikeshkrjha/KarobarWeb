from django.contrib import admin
from karobar.models import Customer, Sales, Purchase, Supplier, SupplierPayment, PaymentsReceived


# The model classes for KarobarWeb app


class CustomerAdmin(admin.ModelAdmin):
    fields = ('customer_fname', 'customer_lname', 'email', 'phone_number')
    list_display = ('customer_fname', 'customer_lname',
                    'email', 'phone_number')


class SupplierAdmin(admin.ModelAdmin):
    fields = ('supplier_name', 'phone_number', 'email', 'supplier_city')
    list_display = ('supplier_name', 'phone_number', 'email', 'supplier_city')


class SalesAdmin(admin.ModelAdmin):
    fields = ('transaction_title', 'transaction_date',
              'transaction_amount', 'transaction_is_cash', 'sold_to')
    list_display = ('transaction_title', 'transaction_date',
                    'transaction_amount', 'transaction_is_cash', 'sold_to')


class PurchaseAdmin(admin.ModelAdmin):
    fields = ('transaction_title', 'transaction_date',
              'transaction_amount', 'transaction_is_cash', 'purchased_from')
    list_display = ('transaction_title', 'transaction_date',
                    'transaction_amount', 'transaction_is_cash', 'purchased_from')


class SupplierPaymentAdmin(admin.ModelAdmin):
    fields = ('description', 'amount', 'payment_date', 'paid_to')
    list_display = ('description', 'amount', 'payment_date', 'paid_to')


class PaymentsReceivedAdmin(admin.ModelAdmin):
    fields = ('description', 'amount', 'payment_date', 'paid_by')
    list_display = ('description', 'amount', 'payment_date', 'paid_by')


# models registration

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierPayment, SupplierPaymentAdmin)
admin.site.register(PaymentsReceived, PaymentsReceivedAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Purchase, PurchaseAdmin)
