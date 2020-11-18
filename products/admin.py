from django.contrib import admin
from .models import ProductGroup, ProductItem, ItemGroup


class ProductGroupAdmin(admin.ModelAdmin):
    list_display = (
        'productcode',
        'productname',
        'product_type',
        'group',
        'price_basis'
    )


class ItemGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ProductItemAdmin(admin.ModelAdmin):
    list_display = (
        'serial',
        'name',
        'price'
    )


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(ItemGroup, ItemGroupAdmin)
