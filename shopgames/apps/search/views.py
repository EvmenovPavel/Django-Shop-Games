from django.shortcuts import render
from django.views.generic import TemplateView
from shopgames.apps.models import *
from django.db.models import Q


class SearchView(TemplateView):
    template_name = "search/search.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     kw = self.request.GET.get("keyword")
    #     results = Product.objects.filter(
    #         Q(title__icontains=kw) | Q(description__icontains=kw) | Q(return_policy__icontains=kw))
    #     print(results)
    #     context["results"] = results
    #     return context
