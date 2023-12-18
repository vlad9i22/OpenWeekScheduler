from django.shortcuts import render
from django.template import loader
# Create your views here.

from .models import Goal, Role

def role_and_goal(request):
    roles_list = Role.objects.all()
    goals_list = Goal.objects.all()
    context = {
        "roles_list": roles_list,
        "goals_list": goals_list,
    }
    return render(request, "WeekScheduler/roles_and_goals.html", context)