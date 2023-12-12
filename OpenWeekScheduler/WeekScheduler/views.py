from django.shortcuts import render

# Create your views here.

def role_and_goal(request):
    return render(request, "WeekScheduler/roles_and_goals.html")