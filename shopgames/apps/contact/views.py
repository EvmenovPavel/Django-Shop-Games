from django.views.generic import TemplateView
from shopgames.apps.utils import EcomMixin


class ContactView(EcomMixin, TemplateView):
    template_name = "contact/contact.html"
    extra_context = {"navitem": "contact"}
