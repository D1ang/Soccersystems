from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'amount',
        'timestamp'
    )


admin.site.register(Payment, PaymentAdmin)
