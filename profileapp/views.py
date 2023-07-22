from django.shortcuts import render
from django.views.generic import CreateView

from profileapp.models import Profile


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
