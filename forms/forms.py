from django import forms
from fotoblog.models import Page


class PageForm (forms.ModelForm):
    class Meta:
        model = Page
        fields = "__all__"
        