from django.db import transaction
from rest_framework import serializers

from .models import Business, BusinessMembership


class BusinessRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = [
            "id",
            "name",  # 🔴 FIXED: Was 'business_name', model uses 'name'
            "business_type",
            "registration_number",
            "tax_identification_number",
            "email",
            "phone_number",
            "country",
            "province",
            "city",
            "physical_address",
            "postal_address",
            "verification_status",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "verification_status",
            "created_at",
        ]

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Business name is required.")
        return value

    def validate_email(self, value):
        return value.strip().lower()

    def validate_country(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Country is required.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user

        # 🔴 FIXED: Added owner=user to prevent IntegrityError
        business = Business.objects.create(
            owner=user,
            **validated_data,
            verification_status=Business.VerificationStatus.PENDING,
        )

        BusinessMembership.objects.create(
            user=user,
            business=business,
            role=BusinessMembership.MembershipRole.OWNER,
        )

        return business