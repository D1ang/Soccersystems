from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Shop(models.Model):
    """
    A shop model for employees to connect to.
    1 shop can have multiple employees.
    """
    company_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal = models.CharField(max_length=6)
    region = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    """
    The employee model to create a
    new employee connected to an User
    A employee can only have 1 user & user only 1 employee
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = PhoneNumberField(null=True, blank=True)
    mobile = PhoneNumberField(null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name
