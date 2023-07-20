from accountapp.forms import AccountUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView


# Create your views here.
def home(request):
    return render(request, 'accountapp/home.html')

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accountapp/create.html'
    success_url = reverse_lazy('accountapp:home')

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'
    success_url = reverse_lazy('accountapp:home')

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})






