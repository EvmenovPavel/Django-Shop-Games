from .views import *
from django.urls import path, include

urlpatterns = [
    # home
    path("", include("shopgames.apps.home.urls")),
    # about
    path("", include("shopgames.apps.about.urls")),
    # search
    path("", include("shopgames.apps.search.urls")),
    # mycart
    path("", include("shopgames.apps.mycart.urls")),
    # contact
    path("", include("shopgames.apps.contact.urls")),
    # product
    path("", include("shopgames.apps.categories.urls")),
    # details
    path("", include("shopgames.apps.details.urls")),
    # addtocart
    path("", include("shopgames.apps.addtocart.urls")),
    # managecart
    path("", include("shopgames.apps.managecart.urls")),
    # emptycart
    path("", include("shopgames.apps.emptycart.urls")),
    # checkout
    path("", include("shopgames.apps.checkout.urls")),
    # khaltirequest
    path("", include("shopgames.apps.khaltirequest.urls")),
    # khaltiverify
    path("", include("shopgames.apps.khaltiverify.urls")),
    # esewarequest
    path("", include("shopgames.apps.esewarequest.urls")),
    # esewaverify
    path("", include("shopgames.apps.esewaverify.urls")),
    # customerregistration
    path("", include("shopgames.apps.registration.urls")),

    # customerlogout
    path("", include("shopgames.apps.logout.urls")),
    # login
    path("", include("shopgames.apps.login.urls")),

    # profile
    path("", include("shopgames.apps.profile.urls")),
    # customerorderdetail
    path("", include("shopgames.apps.derdetail.urls")),
    # passworforgot
    path("", include("shopgames.apps.passwordforgot.urls")),

    # passwordreset
    path("", include("shopgames.apps.passwordreset.urls")),
    # admin
    path("", include("shopgames.apps.admin.urls")),

]
