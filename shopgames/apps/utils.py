from django import forms
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from .models import Cart


class MyPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp)
        )


password_reset_token = MyPasswordResetTokenGenerator()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class EcomMixin(object):
    def dispatch(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            if request.user.is_authenticated and request.user.customer:
                cart_obj.customer = request.user.customer
                cart_obj.save()
        return super().dispatch(request, *args, **kwargs)
