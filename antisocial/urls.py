from django.conf.urls import patterns, url
from .views import ego

urlpatterns = patterns(
    '',
    url(r'^ego/$', ego, name='antisocial_ego'),
)
