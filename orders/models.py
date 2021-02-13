from django.conf import settings
from django.db import models
from accounts.models import Shop
from products.models import ProductItem


class OrderItem(models.Model):
    """
    A model for the order items
    to be collected by the order.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=25)
    ordered = models.BooleanField(default=False)

    @property
    def total_cost(self):
        return self.quantity * self.item.price

    def get_total_item_price(self):
        return self.item.price

    def __str__(self):
        return self.item.name


class Order(models.Model):
    """
    A model to collect
    the order items in 1 order
    """
    STATUS = (
        ('requested', 'Requested'),
        ('pending', 'Pending'),
        ('finished', 'Finished')
    )

    id_code = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='requested', max_length=10)
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






    # This is my custom JSON Response
    def serializeCustom(self):
        items = list(OrderItem.objects.filter(order__pk=self.id).values('item', 'quantity'))

        for item in items:
            item["Opdrachten::kf_web_order_id"] = self.id_code
            item["Opdrachten::artikelnummer"] = item.pop("item")
            item["Opdrachten::aantal_gereserveerd"] = item.pop("quantity")     

        data = {
            "fieldData": {
                "kp_orderbeheer_id": self.id_code,
                "order_soort": "Order",
                "order_status": "Bevestigd",
                "omschrijving": "Test order",
                "referentie": "Ingram",
                "kf_relatiebeheer_id": 92887518,
                # "shop": list(Shop.objects.filter(order__pk=self.id).values('company_name')),
            },
            "portalData": {
                "portal": items
            }
        }
        return data
