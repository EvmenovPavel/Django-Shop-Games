from django.views.generic import TemplateView
from shopgames.apps.utils import EcomMixin


class AboutView(EcomMixin, TemplateView):
    template_name = "about/about.html"
    extra_context = {"nav_item_about": "active"}

    # template_name = None
    # template_engine = None
    # response_class = TemplateResponse
    # content_type = None
    # extra_context = {"":""}
    # permanent = False
    # url = None
    # pattern_name = None
    # query_string = False
