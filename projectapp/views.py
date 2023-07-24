from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


# Create your views here.
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())
        return super().get_context_data(object_list=object_list)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = "projectapp/list.html"
    paginate_by = 5


