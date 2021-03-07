from django.views.generic import DetailView
from django.shortcuts import redirect
from shopgames.apps.models import *


class OrderDetailView(DetailView):
    template_name = "derdetail/derdetail.html"
    model = Order
    context_object_name = "ord_obj"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            order_id = self.kwargs["pk"]
            order = Order.objects.get(id=order_id)
            if request.user.customer != order.cart.customer:
                return redirect("profile")
        else:
            return redirect("/login/?next=/profile/")

        return super().dispatch(request, *args, **kwargs)
