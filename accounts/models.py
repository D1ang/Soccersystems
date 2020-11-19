from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Shop(models.Model):
    """
    The employee model to create a
    new employee connected to an User
    A employee can only have 1 user & user only 1 employee
    """
    company_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50, blank=True, null=True)
    postal = models.CharField(max_length=6)

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
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    phone = PhoneNumberField(null=True, blank=True)
    mobile = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.last_name
