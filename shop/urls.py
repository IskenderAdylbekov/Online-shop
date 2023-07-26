from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(authentication_form=LoginForm),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.index, name="index"),
    path("<slug:category_slug>/", views.index, name="items_by_category"),
    path("<int:id>/<slug:slug>/", views.item_detail, name="detail"),
]
