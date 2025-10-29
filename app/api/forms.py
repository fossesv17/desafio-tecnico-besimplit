from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 text-xl',
                'placeholder' : 'Titulo de la tarea'
            }),
            'description': forms.Textarea(attrs={
                'class': 'border rounded px-3 py-2 w-full h-24 focus:outline-none focus:ring-2 focus:ring-brand text-xl',
                'rows' : 3,
                'placeholder' : 'Descripción de la tarea'
            }),
        }