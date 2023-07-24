from django.shortcuts import render
from django.views.generic import CreateView

from projectapp.models import Project


# Create your views here.
class ProjectCreateView(CreateView):
    model = Project