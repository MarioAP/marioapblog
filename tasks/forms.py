from django import forms
from django.forms import ModelForm
from .models import TaskModel


class TaskForm(forms.ModelForm):

    class Meta:
        model = TaskModel
        fields = '__all__'
