from sysconfig import get_config_h_filename
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Goal, Role
from .forms import Goal_form

def handle_new_goal(request):
    if request.method == "POST":
        form = Goal_form(1, request.POST)
        if form.is_valid():
            add_goal = Goal(goal_text=form.cleaned_data['goal_text'], role_id=Role.objects.get(pk=1))
            add_goal.save()
            return HttpResponseRedirect("/WeekScheduler/")
        return render(request, "WeekScheduler/test.html")


def role_and_goal(request):
    roles_list = Role.objects.all()
    goals_list = Goal.objects.all()
    form = Goal_form(1)
    context = {
        "roles_list": roles_list,
        "goals_list": goals_list,
        "form": form,
    }
    return render(request, "WeekScheduler/roles_and_goals.html", context)