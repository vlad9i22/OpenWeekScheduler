from django import forms 

class Goal_form(forms.Form):
    
    def __init__(self, role, *args, **kwargs):
        super(Goal_form, self).__init__(*args, **kwargs)


    goal_text = forms.CharField(label='', max_length=300)
    # role_id = forms.IntegerField()