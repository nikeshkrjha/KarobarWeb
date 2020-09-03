from django.db import models
from django.utils import timezone

# Create your models here.


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=50, verbose_name="Email", blank=True)
    phone_number = models.CharField(
        max_length=13, verbose_name="Phone Number", blank=False)
    supplier_city = models.CharField(
        max_length=50, blank=False, verbose_name="City")
    supplier_zipcode = models.CharField(
        max_length=5, blank=True, verbose_name="Zip Code")

    def __str__(self):
        return self.supplier_name


class Customer(models.Model):
    customer_fname = models.CharField(
        max_length=50, blank=False, verbose_name="First Name")
    customer_lname = models.CharField(
        max_length=50, blank=False, verbose_name="Last Name")
    email = models.EmailField(max_length=50, verbose_name="Email", blank=True)
    phone_number = models.CharField(
        max_length=13, verbose_name="Phone Number", blank=False)
    customer_city = models.CharField(
        max_length=50, blank=False, verbose_name="City")
    customer_zipcode = models.CharField(
        max_length=5, blank=True, verbose_name="Zip code")

    def __str__(self):
        return self.customer_fname + " " + self.customer_lname


# The sales model. Represents the sales made to customers.

class Sales(models.Model):
    transaction_title = models.CharField(
        max_length=200, blank=False, verbose_name="Title")
    transaction_date = models.DateTimeField(
        auto_now_add=False, verbose_name="Date", default=timezone.now)
    transaction_amount = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Amount")
    transaction_is_cash = models.BooleanField(
        blank=False, null=False, verbose_name="Cash", default=True)
    sold_to = models.ForeignKey(
        Customer, related_name='+', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.transaction_title + " for " + str(self.transaction_amount)


# The purchase model. Represents the purchase made from suppliers.

class Purchase(models.Model):
    transaction_title = models.CharField(
        max_length=200, blank=False, verbose_name="Title")
    transaction_date = models.DateTimeField(
        auto_now_add=False, verbose_name="Date", default=timezone.now)
    transaction_amount = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Amount")
    transaction_is_cash = models.BooleanField(
        blank=False, null=False, verbose_name="Cash", default=True)
    purchased_from = models.ForeignKey(
        Supplier, related_name='+', on_delete=models.CASCADE)
    transaction_is_cash = models.BooleanField(
        blank=False, null=False, verbose_name="Cash", default=True)

    def __str__(self):
        return self.transaction_title + " for " + str(self.transaction_amount)


# The SupplierPayment model. Represents the payments made to suppliers.
class SupplierPayment(models.Model):
    description = models.CharField(max_length=200, blank=False, null=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(
        auto_now_add=False, default=timezone.now)
    paid_to = models.name = models.ForeignKey(
        'Supplier', related_name='+', on_delete=models.CASCADE)


# The PaymentsReceived model. Represents the payments received from customers.
class PaymentsReceived(models.Model):
    description = models.CharField(max_length=200, blank=False, null=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(
        auto_now_add=False, default=timezone.now)
    paid_by = models.name = models.ForeignKey(
        'Customer', related_name='+', on_delete=models.CASCADE)
