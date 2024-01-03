from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.role_and_goal, name="role_and_goal"),
    path("handle_goal_add", views.handle_new_goal, name="add_goal"),
]