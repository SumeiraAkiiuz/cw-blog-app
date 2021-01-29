from django.urls import path
from .views import RegisterUser, Profile_update
from rest_framework import views as rest_views

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/<id>", Profile_update, name="profile"),
    path("profile/update/", Profile_update, name="update-profile")
]
