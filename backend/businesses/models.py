import os
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class Business(models.Model):

    class BusinessType(models.TextChoices):
        RETAILER = "RETAILER", "Retailer"
        WHOLESALER = "WHOLESALER", "Wholesaler"

    class VerificationStatus(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PENDING = "PENDING", "Pending verification"
        UNDER_REVIEW = "UNDER_REVIEW", "Under review"
        VERIFIED = "VERIFIED", "Verified"
        REJECTED = "REJECTED", "Rejected"
        SUSPENDED = "SUSPENDED", "Suspended"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="owned_businesses",
    )

    name = models.CharField(max_length=200)
    business_type = models.CharField(max_length=20, choices=BusinessType.choices)
    registration_number = models.CharField(max_length=100, blank=True)
    tax_identification_number = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=2, default="ZW")
    province = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    physical_address = models.TextField()
    postal_address = models.TextField(blank=True)

    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.DRAFT,
    )
    rejection_reason = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    submitted_at = models.DateTimeField(null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["business_type", "verification_status"]),
            models.Index(fields=["country", "city"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.get_business_type_display()})" # type: ignore


class BusinessMembership(models.Model):

    class MembershipRole(models.TextChoices):
        OWNER = "OWNER", "Owner"
        MANAGER = "MANAGER", "Manager"
        STAFF = "STAFF", "Staff"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="business_memberships",
    )
    business = models.ForeignKey(
        Business,
        on_delete=models.PROTECT,
        related_name="memberships",
    )
    role = models.CharField(max_length=20, choices=MembershipRole.choices)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "business"],
                name="unique_user_business_membership",
            ),
        ]

    def __str__(self):
        return f"{self.user} - {self.business} - {self.role}"


def business_document_upload_path(instance, filename):
    extension = os.path.splitext(filename)[1].lower()
    return (
        f"business_documents/"
        f"{instance.business_id}/"
        f"{instance.id or 'pending'}"
        f"{extension}"
    )


class BusinessDocument(models.Model):

    class DocumentType(models.TextChoices):
        COMPANY_REGISTRATION = "COMPANY_REGISTRATION", "Company registration certificate"
        TAX_CLEARANCE = "TAX_CLEARANCE", "Tax clearance certificate"
        TAX_REGISTRATION = "TAX_REGISTRATION", "Tax registration document"
        BUSINESS_LICENSE = "BUSINESS_LICENSE", "Business licence"
        PROOF_OF_ADDRESS = "PROOF_OF_ADDRESS", "Proof of business address"
        IDENTITY_DOCUMENT = "IDENTITY_DOCUMENT", "Owner or authorised representative identity"
        OTHER = "OTHER", "Other supporting document"

    class ReviewStatus(models.TextChoices):
        PENDING = "PENDING", "Pending review"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    business = models.ForeignKey(
        Business,
        on_delete=models.PROTECT,
        related_name="documents",
    )
    document_type = models.CharField(max_length=30, choices=DocumentType.choices)
    title = models.CharField(max_length=200)
    file = models.FileField(
        upload_to=business_document_upload_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf", "jpg", "jpeg", "png"])
        ],
    )
    document_number = models.CharField(max_length=100, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    
    review_status = models.CharField(
        max_length=20,
        choices=ReviewStatus.choices,
        default=ReviewStatus.PENDING,
    )
    reviewer_notes = models.TextField(blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business.name} - {self.title}"