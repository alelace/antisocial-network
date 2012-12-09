from django.contrib import admin
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'asn.views.home', name='home'),
    url(r'^asn/', include('asn.antisocial.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
