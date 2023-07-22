from django.shortcuts import render
from django.views.generic import CreateView

from articleapp.models import Article


# Create your views here.
class ArticleCreateView(CreateView):
    model = Article