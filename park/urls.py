from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from park_app import views
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    url(r'^howto/$', views.index, name='index'),
    url(r'^$', views.gallery, name=''),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
)
