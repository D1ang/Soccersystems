from django.contrib import admin
from .models import Shop, Employee


class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'city',
        'region'
    )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'shop',
        'email'
    )


admin.site.register(Shop, ShopAdmin)
admin.site.register(Employee, EmployeeAdmin)
