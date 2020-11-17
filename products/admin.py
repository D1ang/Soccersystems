from django.contrib import admin
from .models import Product, ProductItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'productcode',
        'productname',
        'product_type',
        'group',
        'price_basis'
    )


class ProductItemAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'price'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
