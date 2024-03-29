from django.conf import settings
from django.db import models
from accounts.models import Shop
from products.models import ProductItem
from django.utils.translation import gettext_lazy as _


class OrderItem(models.Model):
    '''
    A model for the order items
    to be collected by the order.
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    article_id = models.CharField(max_length=8, null=True)
    description = models.CharField(max_length=85, null=True)
    fileMaker_id = models.IntegerField()
    quantity = models.IntegerField(default=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ordered = models.BooleanField(default=False)

    @property
    def total_cost(self):
        return self.quantity * self.price

    def get_total_item_price(self):
        return self.price

    def __str__(self):
        return '%s - %s' % (self.shop, self.article_id)


class Order(models.Model):
    '''
    A model to collect
    the order items in 1 order
    '''
    STATUS = (
        ('request', _('Request')),
        ('production', _('Production')),
        ('backorder', _('Backorder')),
        ('sent', _('Sent'))
    )

    id_code = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='request', max_length=10)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    total = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    comments = models.TextField(max_length=250, blank=True, null=True)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price() * order_item.quantity
        return total

    def __str__(self):
        return self.user.username
