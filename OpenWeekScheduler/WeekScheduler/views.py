from sysconfig import get_config_h_filename
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Goal, Role
from .forms import Goal_form



def handle_new_goal(request):
    if request.method == "POST":
        form = Goal_form(request.POST)
        if form.is_valid():
            add_goal = Goal(goal_text=form.cleaned_data['goal_text'], role_id=Role.objects.get(pk=form.cleaned_data['role']))
            add_goal.save()
            return HttpResponseRedirect("/WeekScheduler/")
        print(form.errors)
        return render(request, "WeekScheduler/test.html")


def role_and_goal(request):
    roles_list = Role.objects.all()
    goals_list = Goal.objects.all()
    forms = []
    for role in roles_list:
        print(type(int(role.pk)))
        forms.append(Goal_form(initial={'role': int(role.pk)}))
    context = {
        "roles_list": roles_list,
        "goals_list": goals_list,
        "roles_form_list": zip(roles_list, forms),
    }
    return render(request, "WeekScheduler/roles_and_goals.html", context)