from django.db import models
from django.conf import settings
from businesses.models import Business
from trading.models import Order, RFQ

class Conversation(models.Model):
    # Who is in the chat?
    retailer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="retailer_conversations"
    )
    wholesaler = models.ForeignKey(
        Business, 
        on_delete=models.CASCADE, 
        related_name="wholesaler_conversations"
    )

    # Optional context (what are they talking about?)
    related_order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True, related_name="conversations"
    )
    related_rfq = models.ForeignKey(
        RFQ, on_delete=models.SET_NULL, null=True, blank=True, related_name="conversations"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"Chat: {self.retailer.username} <-> {self.wholesaler.name}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation, 
        on_delete=models.CASCADE, 
        related_name="messages"
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="sent_messages"
    )
    
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"] # Oldest to newest

    def __str__(self):
        return f"Msg from {self.sender.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"