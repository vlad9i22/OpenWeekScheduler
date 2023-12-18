from django.db import models

# Create your models here.

class Role(models.Model):
    role_name = models.CharField(max_length=100)
    def __str__(self):
        return self.role_name

class Goal(models.Model):
    goal_text = models.CharField(max_length=300)
    color = models.IntegerField(default=0xc1b7b0)
    week_num = models.IntegerField(default=0) # 0 - 6 Monday-Sunday
    day_num = models.IntegerField(default=0)
    number_in_day = models.IntegerField(default=0)
    role_id = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    def __str__(self):
        return self.goal_text
