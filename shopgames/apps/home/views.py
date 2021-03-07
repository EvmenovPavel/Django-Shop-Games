from django.views.generic import TemplateView
from django.core.paginator import Paginator
from shopgames.apps.models import *


class HomeView(EcomMixin, TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myname"] = "Dipak Niroula"
        all_products = Product.objects.all().order_by("-id")
        paginator = Paginator(all_products, 8)
        page_number = self.request.GET.get("page")
        print(page_number)
        product_list = paginator.get_page(page_number)
        context["product_list"] = product_list
        return context
