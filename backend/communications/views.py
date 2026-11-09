from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from businesses.models import Business

class ConversationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Show conversations where the user is either the retailer OR the owner of the wholesaler business
        return Conversation.objects.filter(
            Q(retailer=user) | Q(wholesaler__owner=user)
        ).distinct()

    def perform_create(self, serializer):
        user = self.request.user
        wholesaler_id = self.request.data.get("wholesaler")
        
        # If the user is a retailer, they are creating the chat
        if not hasattr(user, "owned_businesses"):
            wholesaler = get_object_or_404(Business, id=wholesaler_id)
            # Prevent duplicate 1-on-1 chats for the same order/context
            existing = Conversation.objects.filter(
                retailer=user, 
                wholesaler=wholesaler,
                related_order_id=self.request.data.get("related_order")
            ).first()
            if existing:
                return # (In a real app, you'd return the existing one, but DRF needs the create to return an instance)
            
            serializer.save(retailer=user, wholesaler=wholesaler)
        else:
            raise permissions.ValidationError("Wholesalers cannot initiate a conversation with themselves. Retailers initiate.")


class MessageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        conversation_id = self.kwargs.get("conversation_id")
        # Ensure user belongs to the conversation
        conversation = get_object_or_404(
            Conversation, 
            id=conversation_id
        )
        if conversation.retailer != self.request.user and conversation.wholesaler.owner != self.request.user:
            raise permissions.PermissionDenied("You are not part of this conversation.")
            
        return Message.objects.filter(conversation=conversation)

    def perform_create(self, serializer):
        conversation_id = self.kwargs.get("conversation_id")
        conversation = get_object_or_404(Conversation, id=conversation_id)
        
        # Save the message
        message = serializer.save(
            conversation=conversation,
            sender=self.request.user
        )
        
        # Update the conversation's updated_at timestamp so it jumps to the top of the list
        conversation.save()