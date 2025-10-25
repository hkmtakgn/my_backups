from fotoblog.models import Page


def nav_pages (request):
    if request.user.is_authenticated and request.user.is_superuser:
        pages = Page.objects.filter (is_active=True)
    else:
        pages = Page.objects.filter (slug__in=["home","contact","vision"],is_active=True).order_by("id")
    return dict (g_pages=pages,)
