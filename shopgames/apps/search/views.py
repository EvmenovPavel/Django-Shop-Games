from django.views.generic import TemplateView
from shopgames.apps.models import *
from django.db.models import Q
from django.db.models.query import QuerySet


class SearchView(TemplateView):
    template_name = "search/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")

        list = kw.split()

        results = []
        for item in list:
            print("item:", item)
            resunt = Product.objects.filter(
                Q(title__icontains=item) | Q(description__icontains=item) | Q(return_policy__icontains=item))
            if resunt:
                results.append(resunt)

        print("results:", results)

        context["results"] = results
        return context
