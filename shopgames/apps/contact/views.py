from django.shortcuts import render
from django.views.generic import TemplateView
from shopgames.apps.models import *


class ContactView(EcomMixin, TemplateView):
    template_name = "contact/contact.html"
