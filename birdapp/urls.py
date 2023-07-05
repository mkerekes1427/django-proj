from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("upload_observation", views.upload_observation, name="upload_observation"),
    path("bird_email/", views.bird_email, name="bird_email"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout")

]