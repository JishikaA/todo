from django import forms
from django.contrib.auth.models import User

from todo_app.models import Todo1


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo1
        fields ="__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ="__all__"