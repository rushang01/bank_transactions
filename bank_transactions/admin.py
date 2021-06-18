from django.contrib import admin

# Register your models here.
from .models import Payments

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')

admin.site.register(Payments,PaymentAdmin)

