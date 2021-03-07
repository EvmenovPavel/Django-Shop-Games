from django.views.generic import TemplateView
from shopgames.apps.models import *


class CategoriesView(EcomMixin, TemplateView):
    template_name = "categories/categories.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allcategories"] = Category.objects.all()
        return context
