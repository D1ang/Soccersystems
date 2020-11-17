from django.db import models


class Product(models.Model):
    """
    A model for the products
    This can be groups on a product basis
    """
    productcode = models.CharField(max_length=5)
    productname = models.CharField(max_length=30)
    product_type = models.CharField(max_length=25)
    group = models.CharField(max_length=25)
    price_basis = models.CharField(max_length=15)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.productname


class ProductItem(models.Model):
    """
    A model for the product items.
    Urls are slug based.
    """
    slug = models.SlugField()
    name = models.CharField(max_length=25)
    
    description = models.TextField(max_length=70)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name
