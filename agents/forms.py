from django import forms
from leads.models import Agent, User
# from django.contrib.auth.forms import UserCreationForm, UsernameField


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
