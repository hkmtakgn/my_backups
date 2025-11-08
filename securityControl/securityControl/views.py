from django.shortcuts import get_object_or_404, render, redirect
from securityControl.models import Page, Taseron, Ziyaretci, yuk_arac
from forms.forms import TaseronForm, ZiyaretciForm, yukAracForm
# Create your views here.


def page_views(request, page_slug=None, location=None):
    page = None
    pages = None
    title = None
    if page_slug == None:
        title = "Ana Sayfa"
        pages = Page.objects.filter(is_active=True)
        if pages:
            pages = pages
        else:
            pages = ["Sayfa Bulunamadı (Page not found)!"]
    if page_slug:
        if page_slug == "ziyaretci":
            return ziyaretci_views(request, page_slug, location)
        if page_slug == "taseron":
            return taseron_views(request, page_slug, location)
        if page_slug == "yuk-arac":
            return yuk_arac_views(request, page_slug, location)
        else:
            page = get_object_or_404(Page, slug=page_slug, is_active=True)
            title = page.title

    context = dict(
        page_slug=page_slug,
        pages=pages,
        page_title=title,
        page=page,
    )
    return render(request, "pages/page-views.html", context)


def ziyaretci_views(request, page_slug, location=None):
    ziyaretciler = Ziyaretci.objects.all()
    if ziyaretciler:
        ziyaretciler = ziyaretciler
        page_slug = page_slug
    else:
        ziyaretciler = None
        page_slug = page_slug
    if request.method == "POST":
        ziyaretci_form = ZiyaretciForm(request.POST)
        if ziyaretci_form.is_valid():
            ziyaretci_form.save()
            if location:
                return redirect("sc:page-views", page_slug=location)
            else:
                return redirect("sc:page-views", page_slug=page_slug)

    else:
        ziyaretci_form = ZiyaretciForm()
    pages = None
    title = "Ziyaretçi Kayıt"
    context = dict(
        page_title=title,
        pages=pages,
        ziyaretci_form=ziyaretci_form,
        ziyaretciler=ziyaretciler,
        page_slug=page_slug,
    )
    return render(request, "pages/page-views.html", context)


def taseron_views(request, page_slug, location=None):
    ziyaretci_form = ZiyaretciForm()
    ziyaretciler = Ziyaretci.objects.all()
    taseronlar = Taseron.objects.all()
    if taseronlar:
        taseronlar = taseronlar
        page_slug = page_slug
    else:
        taseronlar = None
        page_slug = page_slug
    if request.method == "POST":
        taseron_form = TaseronForm(request.POST)
        if taseron_form.is_valid():
            taseron_form.save()
            if location:
                return redirect("sc:page-views", page_slug=location)
            else:
                return redirect("sc:page-views", page_slug=page_slug)

    else:
        taseron_form = TaseronForm()
    context = dict(
        taseron_form=taseron_form,
        page_slug=page_slug,
        taseronlar=taseronlar,
        ziyaretci_form=ziyaretci_form,
        ziyaretciler=ziyaretciler,
    )
    return render(request, "pages/page-views.html", context)


def yuk_arac_views(request, page_slug, location=None):
    ziyaretci_form = ZiyaretciForm()
    ziyaretciler = Ziyaretci.objects.all()
    yuk_araclari = yuk_arac.objects.filter(is_inside=True)
    if yuk_araclari:
        yuk_araclari = yuk_araclari
    else:
        yuk_araclari = None

    if request.method == "POST":
        yuk_arac_form = yukAracForm(request.POST)
        if yuk_arac_form.is_valid():
            yuk_arac_form.save()
            if location:
                return redirect("sc:page-views", page_slug=location)
            else:
                return redirect("sc:page-views", page_slug=page_slug)

        else:
            yuk_arac_form = yukAracForm()

    else:
        yuk_arac_form = yukAracForm()

    context = dict(
        yuk_arac_form=yuk_arac_form,
        yuk_araclari=yuk_araclari,
        page_slug=page_slug,
        ziyaretci_form=ziyaretci_form,
        ziyaretciler=ziyaretciler,
    )
    return render(request, "pages/page-views.html", context)
