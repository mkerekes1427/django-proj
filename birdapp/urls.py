from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("upload_observation", views.upload_observation, name="upload_observation"),
    path("random_bird/", views.random_bird, name="random_bird"),
    path("profile/", views.profile, name="profile"),
    path("search", views.search, name="search"),
    path("login/", views.login_user, name="login_user"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_user, name="logout_user"),
    path("about", views.about, name="about")

]