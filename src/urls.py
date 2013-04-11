from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import ListView
import desarrolloq
from desarrolloq.models import Caption
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DesarrolloQ_Website.views.home', name='home'),
    # url(r'^DesarrolloQ_Website/', include('DesarrolloQ_Website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',  ListView.as_view(model=Caption, template_name='index.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
