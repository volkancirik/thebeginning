from django.conf.urls.defaults import patterns, include, url
from settings import DOCUMENT_ROOT
from settings import STATIC_ROOT
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
#    (r'^img/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_ROOT}),
#    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': '%s' % DOCUMENT_ROOT, 'show_indexes': True}),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),

    (r'^background/$', 'thebeginning.app.views.background'),
    (r'^video/$', 'thebeginning.app.views.video'),
    (r'^gallery/$', 'thebeginning.app.views.gallery'),
    (r'^director/$', 'thebeginning.app.views.director'),
    (r'^castandcrew/$', 'thebeginning.app.views.castandcrew'),
    (r'^contact/$', 'thebeginning.app.views.contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'thebeginning.app.views.background'), # Should be the last element.

)
