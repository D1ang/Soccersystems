from django.db import models
from django.shortcuts import reverse


class ProductGroup(models.Model):
    """
    A model for the products
    This can be groups on a product basis
    """
    slug = models.SlugField(max_length=15, primary_key=True, unique=True)
    productcode = models.CharField(max_length=5)
    productname = models.CharField(max_length=30)
    sort = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.productname


class ItemGroup(models.Model):
    """
    A model for the product item groups.
    """
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class ItemTag(models.Model):
    """
    A model for the item tags with selectable
    Bootstrap colours.
    """
    TAG_COLOURS = (
        ('danger', 'Red'),
        ('success', 'Green'),
        ('info', 'Blue'),
        ('warning', 'Yellow'),
        ('secondary', 'Gray')
    )

    name = models.CharField(max_length=10)
    colour = models.CharField(choices=TAG_COLOURS, max_length=10, default='Red')

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    """
    A model for the product items.
    Urls are slug based on the slug field.
    """
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    item_group = models.ForeignKey(ItemGroup, null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=8, primary_key=True, unique=True)
    description = models.CharField(max_length=25)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    tag = models.ForeignKey(ItemTag, null=True, blank=True, on_delete=models.SET_NULL)

    def get_add_to_cart_url(self):
        return reverse('orders:add_to_cart', kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('orders:remove_from_cart', kwargs={
            'slug': self.slug
        })

    def _get_name(self):
        # Returns the articles full description.
        return '%s / %s / %s cm' % (self.product_group,
                                    self.description,
                                    self.size)
    name = property(_get_name)

    class Meta:
        ordering = ['product_group', 'description', 'size']

    def __str__(self):
        # Returns the articles full description for valuelists.
        return '%s / %s / %s cm' % (self.product_group,
                                    self.description,
                                    self.size)
