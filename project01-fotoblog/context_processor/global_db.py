from fotoblog.models import Page


def nav_pages (request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            pages = Page.objects.filter (is_active=True)
        elif request.user.is_active:
            pages = Page.objects.filter (is_active=True).exclude (slug="add-page")
        else:
            pages = Page.objects.filter (slug__in=["home","contact","vision"],is_active=True).order_by("id")

    else:
        pages = Page.objects.filter (slug__in=["home","contact","vision"],is_active=True).order_by("id")
    return dict (g_pages=pages,)
