from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("upload_observation", views.upload_observation, name="upload_observation"),
    path("bird_email/", views.bird_email, name="bird_email"),
    path("profile/", views.profile, name="profile"),
    path("search", views.search, name="search"),
    path("login/", views.login_user, name="login_user"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_user, name="logout_user")

]