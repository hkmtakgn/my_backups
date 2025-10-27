from django import forms
from fotoblog.models import Page,Post


class PageForm (forms.ModelForm):
    class Meta:
        model = Page
        fields = "__all__"
        


class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

