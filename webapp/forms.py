from django import forms
from .models import TaskManage


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskManage
        fields = ['description', 'status', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
