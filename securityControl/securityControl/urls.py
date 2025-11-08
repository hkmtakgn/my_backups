from django.urls import path
from securityControl.views import page_views

app_name = "sc"

urlpatterns = [
    path("", page_views, name="page-views"),
    path("<slug:page_slug>/", page_views, name="page-views"),
    path("<slug:page_slug>/<slug:location>", page_views, name="page-views"),
]
