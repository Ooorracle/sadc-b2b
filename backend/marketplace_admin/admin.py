from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ["id", "admin_user", "action", "target_model", "target_id", "created_at"]
    list_filter = ["action", "target_model", "created_at"]
    search_fields = ["admin_user__username", "notes"]
    readonly_fields = ["created_at"] # Prevent admins from altering history