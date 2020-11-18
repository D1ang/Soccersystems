from django.db import models


class ProductGroup(models.Model):
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


class ItemGroup(models.Model):
    """
    A model for the product item groups.
    """
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    """
    A model for the product items.
    Urls are slug based.
    """
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    group = models.ForeignKey(ItemGroup, null=True,
                              blank=True, on_delete=models.SET_NULL)
    serial = models.SlugField()
    description = models.CharField(max_length=25)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def _get_name(self):
        # Returns the articles full description.
        return '%s / %s / %s cm' % (self.product_group,
                                    self.description,
                                    self.size)
    name = property(_get_name)

    class Meta:
        ordering = ['product_group', 'description', 'size']
