from rest_framework import serializers
from .models import Conversation, Message
from businesses.models import Business
from django.contrib.auth import get_user_model

User = get_user_model()

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source="sender.get_full_name", read_only=True)
    
    class Meta:
        model = Message
        fields = ["id", "conversation", "sender", "sender_name", "content", "is_read", "created_at"]
        read_only_fields = ["id", "sender", "is_read", "created_at"]


class ConversationSerializer(serializers.ModelSerializer):
    retailer_name = serializers.CharField(source="retailer.username", read_only=True)
    wholesaler_name = serializers.CharField(source="wholesaler.name", read_only=True)
    
    # Pull in the last message to show in the chat list preview
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = [
            "id", "retailer", "retailer_name", "wholesaler", "wholesaler_name", 
            "related_order", "related_rfq", "last_message", "updated_at"
        ]
        read_only_fields = ["id", "retailer", "updated_at"]

    def get_last_message(self, obj):
        last_msg = obj.messages.order_by("-created_at").first()
        if last_msg:
            return MessageSerializer(last_msg).data
        return None