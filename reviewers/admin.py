from django.contrib import admin

from .models import Reviewer


@admin.register(Reviewer)
class ReviewerModelAdmin(admin.ModelAdmin):
    pass
