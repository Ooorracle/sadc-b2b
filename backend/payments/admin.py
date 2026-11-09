from django.contrib import admin
from .models import PaymentTransaction, DigitalReceipt

class DigitalReceiptInline(admin.StackedInline):
    model = DigitalReceipt
    extra = 0
    readonly_fields = ["receipt_number", "issued_at"]

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "amount", "currency", "payment_method", "status", "created_at"]
    list_filter = ["status", "payment_method", "currency", "created_at"]
    search_fields = ["order__id", "provider_reference"]
    inlines = [DigitalReceiptInline]

@admin.register(DigitalReceipt)
class DigitalReceiptAdmin(admin.ModelAdmin):
    list_display = ["receipt_number", "payment", "issued_at"]
    search_fields = ["receipt_number", "payment__order__id"]