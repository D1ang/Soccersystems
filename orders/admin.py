from django.contrib import admin
from .models import OrderItem, Order


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'user',
        'ordered'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'ordered',
        'status',
    )


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
