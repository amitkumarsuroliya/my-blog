from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic import RedirectView
from my_blog.sitemap import ArticleSitemap, CategorySitemap, StaticViewSitemap

admin.autodiscover()

urlpatterns = patterns('notes.views',
    url(r'^$', 'home', name='home'),
    url(r'^ru/$', RedirectView.as_view(url='/', permanent=True)),
    url(r'^category/(?P<category>[^/]+)/$', 'by_category', name='by_category'),
    url(r'^(?P<slug>[^/]+)/$', 'view_article', name='view_article'),
)

sitemaps = {
    'articles': ArticleSitemap,
    'categories': CategorySitemap,
    'static': StaticViewSitemap,
}

urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
