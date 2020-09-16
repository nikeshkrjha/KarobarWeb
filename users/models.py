from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(
        max_length=100, blank=False, verbose_name="First Name")
    last_name = models.CharField(
        max_length=100, blank=False, verbose_name="Last Name")
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(
        max_length=13, verbose_name="Phone Number", blank=False)
    city = models.CharField(
        max_length=100, blank=False, verbose_name="City")
    state = models.CharField(
        max_length=100, blank=False, verbose_name="City")
    zipcode = models.CharField(
        max_length=5, blank=True, verbose_name="Zip code")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
