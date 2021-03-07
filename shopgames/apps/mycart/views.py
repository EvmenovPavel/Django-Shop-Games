from django.views.generic import TemplateView
from shopgames.apps.models import *


class MyCartView(EcomMixin, TemplateView):
    template_name = "mycart/mycart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context["cart"] = cart
        return context
