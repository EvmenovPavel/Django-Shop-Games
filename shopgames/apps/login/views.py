from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from shopgames.apps.models import Customer
from shopgames.apps.utils import LoginForm


class LoginView(FormView):
    template_name = "login/login.html"

    form_class = LoginForm
    success_url = reverse_lazy("home")

    # form_valid method is a type of post method and is available in createview formview and updateview
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
