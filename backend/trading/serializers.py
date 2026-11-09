from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from .models import RFQ, Offer, Order
from catalogue.models import Product

class RFQSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = RFQ
        fields = [
            "id", "retailer", "wholesaler", "product", "product_name",
            "quantity", "message", "status", "created_at"
        ]
        read_only_fields = ["id", "retailer", "status", "created_at"]

    def validate(self, attrs):
        # Ensure the product actually belongs to the wholesaler they are messaging
        product = attrs.get("product")
        wholesaler = attrs.get("wholesaler")
        if product.business != wholesaler:
            raise serializers.ValidationError("This product does not belong to the selected wholesaler.")
        return attrs


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            "id", "rfq", "unit_price", "total_price", 
            "currency", "valid_until", "message", "status", "created_at"
        ]
        read_only_fields = ["id", "total_price", "status", "created_at"]

    def create(self, validated_data):
        # Auto-calculate total price based on quantity
        rfq = validated_data["rfq"]
        unit_price = validated_data["unit_price"]
        
        validated_data["total_price"] = unit_price * rfq.quantity
        
        # Default validity is 7 days if not provided
        if not validated_data.get("valid_until"):
            validated_data["valid_until"] = timezone.now() + timedelta(days=7)

        # Update RFQ status to Responded
        rfq.status = RFQ.Status.RESPONDED
        rfq.save()

        return super().create(validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id", "retailer", "wholesaler", "offer", 
            "total_amount", "currency", "status", "delivery_address", "created_at"
        ]
        read_only_fields = ["id", "retailer", "total_amount", "currency", "status", "created_at"]