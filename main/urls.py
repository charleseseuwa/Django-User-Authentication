from django.urls import path
from .views import register, home, frontend_register, frontend_login, frontend_logout
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("register2/", frontend_register, name="register2"),
    path('login/', LoginView.as_view(template_name="main/login.html"), name='login'),
    path("logout/", LogoutView.as_view(template_name="main/logout.html"), name="logout"),
    path("login2/", frontend_login, name="login2"),
    path("logout2/", frontend_logout, name="logout2")
]