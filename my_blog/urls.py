from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('my_blog.views',
    url(r'^about/$', 'about', name='about'),
)


urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^', include('notes.urls')),
)