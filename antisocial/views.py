from django.views.generic.base import TemplateView
from lazysignup.decorators import allow_lazy_user


class Ego(TemplateView):
    template_name = 'antisocial/ego.html'
ego = allow_lazy_user(Ego.as_view())
