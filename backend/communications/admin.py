from django.contrib import admin
from .models import Conversation, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ["sender", "content", "created_at"]

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ["id", "retailer", "wholesaler", "related_order", "updated_at"]
    list_filter = ["updated_at"]
    search_fields = ["retailer__username", "wholesaler__name"]
    inlines = [MessageInline]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "conversation", "sender", "content", "is_read", "created_at"]
    list_filter = ["is_read", "created_at"]