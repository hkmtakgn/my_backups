from securityControl.models import Page


def global_pages(request):
  g_pages = Page.objects.filter(is_active=True)
  context = dict(g_pages=g_pages, )
  return context
