from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    class Meta:
        model = Article
        fields = ['image', 'title', 'project', 'content']