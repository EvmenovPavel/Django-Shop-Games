from django.views.generic import TemplateView
from shopgames.apps.utils import EcomMixin


class AboutView(EcomMixin, TemplateView):
    template_name = "about/about.html"
    extra_context = {"navitem": "about"}
