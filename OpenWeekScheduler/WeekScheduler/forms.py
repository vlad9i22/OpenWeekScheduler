from django import forms 



class Goal_form(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(Goal_form, self).__init__(*args, **kwargs)

    goal_text = forms.CharField(label='', max_length=300)
    role = forms.DecimalField(label='')
    # role_id = forms.IntegerField()

class Role_form(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(Role_form, self).__init__(*args, **kwargs)

    role_name = forms.CharField(label='', max_length=100)
    # role_id = forms.IntegerField()