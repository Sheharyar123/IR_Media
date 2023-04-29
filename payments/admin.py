from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["user", "amount", "stripe_payment_id"]
    readonly_fields = ["amount", "user", "user_course", "stripe_payment_id"]
    search_fields = ["amount"]


admin.site.register(Payment, PaymentAdmin)
