from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_verified",
        "is_active",
        "is_staff",
    )
    list_filter = (
        "is_verified",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
    )

    # Use lists to avoid the Pyright/Mypy tuple concat bug
    fieldsets = list(UserAdmin.fieldsets) + [
        (
            "Personal Information",
            {
                "fields": (
                    "phone_number",
                    "address",
                    "city",
                    "country",
                    "is_verified",
                )
            },
        ),
    ]

    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        (
            "Additional Information",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "address",
                    "city",
                    "country",
                )
            },
        ),
    ]