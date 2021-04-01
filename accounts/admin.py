from django.contrib import admin

from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    fieldsets = (
        # General information
        (None, {"fields": ("first_name", "last_name")}),
        # Personal info of user
        ("Personal Info", {"fields": (
            "email",
            "password",
        )}),
        # Permission and accesses of user
        ("Permissions", {
            "fields": ("is_active", "is_admin")
        }),
    )
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )

    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
