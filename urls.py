from django.conf.urls.defaults import patterns, include, url
from thebeginning.settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thebeginning.views.home', name='home'),
    # url(r'^thebeginning/', include('thebeginning.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^img/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_ROOT}),
    (r'^synopsis/$', 'thebeginning.app.views.synopsis'),
    (r'^movie/$', 'thebeginning.app.views.movie'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'thebeginning.app.views.synopsis'), # Should be the last element.
)
