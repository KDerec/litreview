from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.redirect_view),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("home/", auth_views.LoginView.as_view(template_name="home.html"), name="home"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("subscription/", views.subscription, name="subscription"),
    path(
        "delete-user-follow/<int:pk>",
        views.delete_user_follows,
        name="delete-user-follow",
    ),
]
