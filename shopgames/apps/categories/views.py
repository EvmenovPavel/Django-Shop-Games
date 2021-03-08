from django.views.generic import TemplateView
from shopgames.apps.models import Category
from shopgames.apps.utils import EcomMixin


class CategoriesView(EcomMixin, TemplateView):
    template_name = "categories/categories.html"
    extra_context = {"navitem": "categories"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allcategories"] = Category.objects.all()
        return context
