from django.shortcuts import render
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


# Create your views here.
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'
    # success_url =

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

