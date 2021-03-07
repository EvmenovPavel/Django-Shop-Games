from django.views.generic import View
from django.shortcuts import render
from shopgames.apps.models import *


class EsewaRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        context = {
            "order": order
        }
        return render(request, "esewarequest/esewarequest.html", context)
