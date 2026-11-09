from django.db import models
from django.conf import settings
from trading.models import Order

class PaymentTransaction(models.Model):
    class PaymentMethod(models.TextChoices):
        STRIPE = "STRIPE", "Stripe (Card)"
        PAYNOW = "PAYNOW", "PayNow (Zimbabwe)"
        ECOCASH = "ECOCASH", "EcoCash"
        MANUAL = "MANUAL", "Manual Bank Transfer"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        SUCCESSFUL = "SUCCESSFUL", "Successful"
        FAILED = "FAILED", "Failed"
        REFUNDED = "REFUNDED", "Refunded"

    order = models.OneToOneField(
        Order, 
        on_delete=models.PROTECT, 
        related_name="payment"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    
    # The Abstraction Layer
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    provider_reference = models.CharField(
        max_length=255, 
        blank=True, 
        help_text="The transaction ID from Stripe, PayNow, etc."
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.id} for Order #{self.order.id} - {self.status}"


class DigitalReceipt(models.Model):
    payment = models.OneToOneField(
        PaymentTransaction, 
        on_delete=models.CASCADE, 
        related_name="receipt"
    )
    receipt_number = models.CharField(max_length=50, unique=True, blank=True)
    qr_verification_url = models.URLField(
        blank=True, 
        help_text="URL encoded in the QR code for verification"
    )
    issued_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-generate a receipt number if it doesn't exist
        if not self.receipt_number:
            import uuid
            self.receipt_number = f"RCPT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Receipt {self.receipt_number} for Order #{self.payment.order.id}"
