from django.contrib import admin
from fotoblog.models import Page



@admin.register(Page)
class PageAdmin (admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]

