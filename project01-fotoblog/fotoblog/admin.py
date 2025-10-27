from django.contrib import admin
from fotoblog.models import Page,Post



@admin.register(Page)
class PageAdmin (admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]


@admin.register (Post)
class PostAdmin (admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]

