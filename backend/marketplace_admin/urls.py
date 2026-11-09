from django.urls import path
from .views import (
    PlatformOverviewAPIView,
    AdminVerificationQueueAPIView,
    AdminUpdateVerificationAPIView,
    AdminAuditLogListAPIView
)

app_name = "marketplace_admin"

urlpatterns = [
    path("overview/", PlatformOverviewAPIView.as_view(), name="platform-overview"),
    path("verifications/", AdminVerificationQueueAPIView.as_view(), name="verification-queue"),
    path("verifications/<int:business_id>/action/", AdminUpdateVerificationAPIView.as_view(), name="update-verification"),
    path("audit-logs/", AdminAuditLogListAPIView.as_view(), name="audit-logs"),
]