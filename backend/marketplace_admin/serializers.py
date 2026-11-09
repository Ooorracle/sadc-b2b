from rest_framework import serializers
from .models import AuditLog
from businesses.models import Business, BusinessDocument
from accounts.models import User
from trading.models import Order

class AuditLogSerializer(serializers.ModelSerializer):
    admin_name = serializers.CharField(source="admin_user.username", read_only=True)

    class Meta:
        model = AuditLog
        fields = "__all__"
        read_only_fields = ["created_at"]

class AdminBusinessSerializer(serializers.ModelSerializer):
    owner_email = serializers.CharField(source="owner.email", read_only=True)

    class Meta:
        model = Business
        fields = [
            "id", "name", "business_type", "owner_email", 
            "verification_status", "created_at"
        ]
        read_only_fields = ["id", "created_at"]

class AdminOrderSerializer(serializers.ModelSerializer):
    retailer_email = serializers.CharField(source="retailer.email", read_only=True)
    wholesaler_name = serializers.CharField(source="wholesaler.name", read_only=True)

    class Meta:
        model = Order
        fields = [
            "id", "retailer_email", "wholesaler_name", 
            "total_amount", "currency", "status", "created_at"
        ]