from django.conf.urls import patterns, url
from .views import ego, logout

urlpatterns = patterns(
    '',
    url(r'^ego/$', ego, name='antisocial_ego'),
    url(r'^logout/$', logout, name='antisocial_logout')
)
