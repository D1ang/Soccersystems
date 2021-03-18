from django.contrib import admin
from .models import OrderItem, Order


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'article_id',
        'item',
        'quantity',
        'shop',
        'ordered'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'shop',
        'date',
        'delivery_date',
        'ordered',
        'status',
    )


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
