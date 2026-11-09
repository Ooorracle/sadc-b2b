from rest_framework import serializers
from .models import PaymentTransaction, DigitalReceipt

class DigitalReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalReceipt
        fields = ["receipt_number", "qr_verification_url", "issued_at"]

class PaymentTransactionSerializer(serializers.ModelSerializer):
    receipt = DigitalReceiptSerializer(read_only=True)

    class Meta:
        model = PaymentTransaction
        fields = [
            "id", "order", "amount", "currency", 
            "payment_method", "provider_reference", 
            "status", "created_at", "receipt"
        ]
        read_only_fields = ["id", "amount", "currency", "status", "created_at"]