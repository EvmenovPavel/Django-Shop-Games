from django.views.generic import TemplateView
from shopgames.apps.models import Product
from shopgames.apps.utils import EcomMixin


class DetailsView(EcomMixin, TemplateView):
    template_name = "details/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs["slug"]
        product = Product.objects.get(slug=url_slug)
        product.view_count += 1
        product.save()
        context["product"] = product
        return context
