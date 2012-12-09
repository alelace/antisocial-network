from django.contrib import admin
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'asn.views.home', name='asn_home'),
    url(r'^antisocial/', include('antisocial.urls')),
    url(r'^convert/', include('lazysignup.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
