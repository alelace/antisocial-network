from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from lazysignup.decorators import allow_lazy_user


class Ego(TemplateView):
    template_name = 'antisocial/ego.html'
ego = allow_lazy_user(Ego.as_view())


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('asn_home'))
