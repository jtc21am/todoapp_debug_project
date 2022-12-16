from django import forms
from django.forms import ModelForm
from todoapp.models import Task

class TaskForm(ModelForm):
    # description = forms.CharField(label='Action', max_length=255, widget=forms.TextInput(attrs={'size': '50'}))
    class Meta:
        model = Task
        fields = ['description']
        labels = {
            'description':'New Task',
        }

class UpdateForm(forms.Form):
    description = forms.CharField(label='Action', max_length=255, widget=forms.TextInput(attrs={'size': '50'}))

class NoteForm(forms.Form):
    text = forms.CharField(label='Action', max_length=255, widget=forms.TextInput(attrs={'size': '50'}))

class CommentForm(forms.Form):
    content = forms.CharField(label='Action', max_length=255, widget=forms.Textarea(attrs={'rows': '10', 'cols': '40'}))

class TagForm(forms.Form):
    name = forms.CharField(label='Action', max_length=30, widget=forms.TextInput(attrs={'size': '30'}))
