from django.contrib import admin
from .models import ProductGroup, ProductItem, ItemGroup, ItemTag


class ProductGroupAdmin(admin.ModelAdmin):
    ordering = ['sort']
    list_display = (
        'sort',
        'productcode',
        'productname'
    )


class ItemGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ItemTagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'colour'
    )


class ProductItemAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'item_group',
        'price'
    )


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ItemGroup, ItemGroupAdmin)
admin.site.register(ItemTag, ItemTagAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
