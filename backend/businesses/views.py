from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Business
from .serializers import BusinessRegistrationSerializer


class BusinessRegistrationAPIView(generics.CreateAPIView):
    serializer_class = BusinessRegistrationSerializer
    permission_classes = [IsAuthenticated]


class MyBusinessesAPIView(generics.ListAPIView):
    serializer_class = BusinessRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Returns businesses where the current user is an active member
        return Business.objects.filter(
            memberships__user=self.request.user,
            memberships__is_active=True,
        ).distinct().order_by("-created_at")