from django.views.generic import TemplateView
from shopgames.apps.models import *


class AboutView(EcomMixin, TemplateView):
    template_name = "about/about.html"
