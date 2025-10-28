from django.urls import path
from fotoblog.views import page_views

from django.conf.urls.static import static
from django.conf import settings

app_name = "fotoblog"

urlpatterns = [
    path("",page_views,name="home_views"),
    path("<slug:page_slug>/",page_views,name="page_views"),
    path("<slug:page_slug>/<slug:post_slug>",page_views,name="page_views"),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



