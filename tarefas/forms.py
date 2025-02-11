from django import forms

from .models import task

class Taskform(forms.ModelForm):
    
    class Meta:
        model = task
        fields =('titulo' , 'tarefas' )
        
