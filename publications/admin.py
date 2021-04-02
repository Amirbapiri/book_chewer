from django.contrib import admin

from .models import Publication


@admin.register(Publication)
class PublicationModelAdmin(admin.ModelAdmin):
    fieldsets = (
        # Personal info of user
        ("Publication Information", {"fields": (
            "user",
            "name",
            "reg_number",
        )}),
    )
    list_display = (
        "user",
        "name",
        "reg_number",
        "date_of_create",
    )

    search_fields = (
        "name",
        "reg_number"
    )
