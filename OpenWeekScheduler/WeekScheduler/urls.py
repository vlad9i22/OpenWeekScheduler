from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.role_and_goal, name="role_and_goal"),
]