from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    class ActionType(models.TextChoices):
        APPROVE_BUSINESS = "APPROVE_BUSINESS", "Approved Business"
        REJECT_BUSINESS = "REJECT_BUSINESS", "Rejected Business"
        SUSPEND_USER = "SUSPEND_USER", "Suspended User"
        MODERATE_PRODUCT = "MODERATE_PRODUCT", "Moderated Product"
        RESOLVE_DISPUTE = "RESOLVE_DISPUTE", "Resolved Dispute"
        SYSTEM_CONFIG = "SYSTEM_CONFIG", "System Configuration Change"

    admin_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="audit_logs"
    )
    action = models.CharField(max_length=50, choices=ActionType.choices)
    target_model = models.CharField(max_length=50, help_text="e.g., 'Business', 'Product'")
    target_id = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.admin_user} - {self.action} - {self.created_at}"
