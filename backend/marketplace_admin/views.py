from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.utils import timezone

from .models import AuditLog
from .serializers import AuditLogSerializer, AdminBusinessSerializer, AdminOrderSerializer
from businesses.models import Business
from accounts.models import User
from trading.models import Order

# Helper permission: Ensure only staff can access
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class PlatformOverviewAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        # Simple aggregated stats
        total_users = User.objects.count()
        total_businesses = Business.objects.count()
        pending_verifications = Business.objects.filter(
            verification_status=Business.VerificationStatus.PENDING
        ).count()
        
        # Financials
        paid_orders = Order.objects.filter(status=Order.Status.PAID)
        gross_volume = paid_orders.aggregate(total=Sum('total_amount'))['total'] or 0.00

        return Response({
            "stats": {
                "total_users": total_users,
                "total_businesses": total_businesses,
                "pending_verifications": pending_verifications,
                "gross_volume": gross_volume,
                "currency": "USD" # Assuming USD base
            }
        })


class AdminVerificationQueueAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminBusinessSerializer
    queryset = Business.objects.filter(
        verification_status__in=[
            Business.VerificationStatus.PENDING,
            Business.VerificationStatus.UNDER_REVIEW
        ]
    ).order_by("created_at")


class AdminUpdateVerificationAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, business_id):
        business = get_object_or_404(Business, id=business_id)
        action = request.data.get("action") # "approve" or "reject"
        reason = request.data.get("reason", "")

        if action == "approve":
            business.verification_status = Business.VerificationStatus.VERIFIED
            business.verified_at = timezone.now()
            log_action = AuditLog.ActionType.APPROVE_BUSINESS
        elif action == "reject":
            business.verification_status = Business.VerificationStatus.REJECTED
            business.rejection_reason = reason
            log_action = AuditLog.ActionType.REJECT_BUSINESS
        else:
            return Response({"error": "Invalid action. Use 'approve' or 'reject'."}, status=400)

        business.save()

        # Create Audit Log
        AuditLog.objects.create(
            admin_user=request.user,
            action=log_action,
            target_model="Business",
            target_id=business.id,
            notes=reason
        )

        return Response({"message": f"Business {action}d successfully."})


class AdminAuditLogListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AuditLogSerializer
    queryset = AuditLog.objects.all()