from django.contrib import admin
from securityControl.models import Ziyaretci, Page, Taseron, yuk_arac

# Register your models here.


@admin.register(Ziyaretci)
class ZiyaretciAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "tc_kimlik_no",
    ]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]


@admin.register(Taseron)
class TaseronAdmin(admin.ModelAdmin):
    list_display = [
        "firma_adi",
        "is_inside",
    ]


@admin.register(yuk_arac)
class YukAracAdmin(admin.ModelAdmin):
    list_display = [
        "sofor",
        "cekici_plaka",
        "dorse_plaka",
        "firma_adi",
        "arac_turu",
        "is_inside",
        "created_at",
        "updated_at",
    ]
