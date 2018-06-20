
from django.forms import ModelForm

from .models import Task
from django import forms


# class UserForm(ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput)

# 	class Meta:
# 		model = Userprofile
# 		fields = ['username', 'email', 'password']

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['task_name', 'complete_by']