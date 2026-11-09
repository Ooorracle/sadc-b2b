from django.contrib import admin
from django.utils import timezone

from .models import Business, BusinessMembership, BusinessDocument


class BusinessMembershipInline(admin.TabularInline):
    model = BusinessMembership
    extra = 0
    autocomplete_fields = ["user"]
    fields = ["user", "role", "is_active", "created_at"]
    readonly_fields = ["created_at"]


class BusinessDocumentInline(admin.TabularInline):
    model = BusinessDocument
    extra = 0
    fields = ["title", "document_type", "review_status", "uploaded_at"]
    readonly_fields = ["uploaded_at"]
    show_change_link = True


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "business_type",
        "owner",
        "country",
        "city",
        "verification_status",
        "is_active",
        "created_at",
    ]
    list_filter = [
        "business_type",
        "verification_status",
        "country",
        "is_active",
    ]
    search_fields = [
        "name",
        "registration_number",
        "tax_identification_number",
        "email",
        "phone_number",
        "city",
        "owner__email",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
        "submitted_at",
        "verified_at",
    ]
    
    fieldsets = [
        (
            "Business Information",
            {
                "fields": [
                    "name",
                    "business_type",
                    "owner",
                    "registration_number",
                    "tax_identification_number",
                ]
            },
        ),
        (
            "Contact Information",
            {
                "fields": [
                    "email",
                    "phone_number",
                    "country",
                    "province",
                    "city",
                    "physical_address",
                    "postal_address",
                ]
            },
        ),
        (
            "Verification",
            {
                "fields": [
                    "verification_status",
                    "rejection_reason",
                    "submitted_at",
                    "verified_at",
                    "is_active",
                ]
            },
        ),
        (
            "Timestamps",
            {
                "fields": ["created_at", "updated_at"]
            },
        ),
    ]

    inlines = [
        BusinessMembershipInline,
        BusinessDocumentInline,
    ]
    list_per_page = 25
    date_hierarchy = "created_at"
    ordering = ["-created_at"]

    actions = [
        "mark_under_review",
        "approve_businesses",
        "reject_businesses",
        "suspend_businesses",
    ]

    @admin.action(description="Mark selected businesses as under review")
    def mark_under_review(self, request, queryset):
        queryset.update(verification_status=Business.VerificationStatus.UNDER_REVIEW)

    @admin.action(description="Approve selected businesses")
    def approve_businesses(self, request, queryset):
        queryset.update(
            verification_status=Business.VerificationStatus.VERIFIED,
            verified_at=timezone.now(),
            rejection_reason="",
        )

    @admin.action(description="Reject selected businesses")
    def reject_businesses(self, request, queryset):
        queryset.update(
            verification_status=Business.VerificationStatus.REJECTED,
            verified_at=None,
        )

    @admin.action(description="Suspend selected businesses")
    def suspend_businesses(self, request, queryset):
        queryset.update(verification_status=Business.VerificationStatus.SUSPENDED)


@admin.register(BusinessMembership)
class BusinessMembershipAdmin(admin.ModelAdmin):
    list_display = ["user", "business", "role", "is_active", "created_at"]
    list_filter = ["role", "is_active", "created_at"]
    search_fields = [
        "user__email",
        "user__first_name",
        "user__last_name",
        "business__name",
    ]
    readonly_fields = ["created_at"]
    autocomplete_fields = ["user", "business"]
    list_per_page = 25


@admin.register(BusinessDocument)
class BusinessDocumentAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "business",
        "document_type",
        "review_status",
        "uploaded_at",
    ]
    list_filter = ["document_type", "review_status", "uploaded_at"]
    search_fields = [
        "title",
        "document_number",
        "business__name",
        "business__registration_number",
    ]
    readonly_fields = ["uploaded_at", "updated_at"]
    fieldsets = [
        (
            "Document Information",
            {
                "fields": [
                    "business",
                    "document_type",
                    "title",
                    "file",
                    "document_number",
                    "issue_date",
                    "expiry_date",
                ]
            },
        ),
        (
            "Review",
            {
                "fields": ["review_status", "reviewer_notes"]
            },
        ),
        (
            "Timestamps",
            {
                "fields": ["uploaded_at", "updated_at"]
            },
        ),
    ]
    autocomplete_fields = ["business"]
    list_per_page = 25
    ordering = ["-uploaded_at"]