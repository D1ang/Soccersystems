from django.contrib import admin
from .models import ProductGroup, ProductItem, ItemGroup


class ProductGroupAdmin(admin.ModelAdmin):
    list_display = (
        'productcode',
        'productname'
    )


class ItemGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ProductItemAdmin(admin.ModelAdmin):
    list_display = (
        'serial',
        'name',
        'item_group',
        'price'
    )


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(ItemGroup, ItemGroupAdmin)
