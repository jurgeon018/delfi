from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.controllers import *
from core.order_api import *
from core.pay import * 
from core.views import * 
from django.contrib import admin
from core.admin import (
  manager_admin_site,
)
from filebrowser.sites import site
from django.views.i18n import JavaScriptCatalog
from django.contrib.sitemaps.views import sitemap 
from django.views.generic import TemplateView
from core.sitemaps import PostSitemap, StaticViewSitemap

sitemaps = {
  'posts': PostSitemap,
  'static':StaticViewSitemap,
}



urlpatterns = [

  path('test_mail/', test_mail, name='test_mail'),

  path('rosetta/',           include('rosetta.urls')),
  path('tinymce/',           include('tinymce.urls')),
  path('i18n/',              include('django.conf.urls.i18n')),
  path('robots.txt/',        TemplateView.as_view(template_name="robots.txt"), name='robots'),
  path('sitemap.xml/',       sitemap, {'sitemaps':sitemaps}),
  path('jsi18n/',            JavaScriptCatalog.as_view(), name='javascript-catalog'),
  path('admin/filebrowser/', site.urls),

  path('set_lang/<lang>/',   set_lang,       name="set_lang"),
  path('set_params/',        set_params,     name='set_params'),
  path('get_seats/',         get_seats,      name="get_seats"),
  path('create_order/',      create_order,   name='create_order'),
  path('pay/',               pay,            name='pay'),
  path('pay_callback/',      pay_callback,   name='pay_callback'),
  path('create_multiple_races/', create_multiple_races, name='create_multiple_races'),

  path('create_bus_comment/<bus_pk>/', create_bus_comment, name='create_bus_comment'),
  path("create_europe_order/" , create_europe_order, name="create_europe_order"),
  path("create_bus_order/" , create_bus_order, name="create_bus_order"),
  path("create_contact/" ,     create_contact,   name="create_contact"),
]
urlpatterns += i18n_patterns(
  path('admin+/',       admin.site.urls),
  path('admin/',        manager_admin_site.urls),
  path('',              index,        name='index'),
  path('blog/',         blog,         name='blog'),
  path('post/<pk>',     post_detail,  name='post_detail'),
  path('contact_us/',   contact_us,   name='contact_us'),
  path('park/',         park,         name='park'),
  path('order/',        order,        name='order'),
  path('about_us/',     about_us,     name='about_us'),
  path('thank_you/',    thank_you,    name='thank_you'),
  path('404/',          page404,      name="page404"),
  prefix_default_language=True,
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


