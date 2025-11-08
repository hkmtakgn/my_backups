from django import forms
from django.db.models import fields
from securityControl.models import Ziyaretci, Taseron, yuk_arac


class ZiyaretciForm(forms.ModelForm):

  class Meta:
    model = Ziyaretci
    fields = "__all__"


class TaseronForm(forms.ModelForm):

  class Meta:
    model = Taseron
    fields = "__all__"

    exclude = ["is_inside", "is_outside"]


class yukAracForm(forms.ModelForm):

  class Meta:
    model = yuk_arac
    fields = "__all__"

    exclude = ["is_inside", "is_outside"]
