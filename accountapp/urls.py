from accountapp.views import home, AccountCreateView
from django.urls import path

app_name = 'accountapp'

urlpatterns = [
    path('home/', home, name='home'),
    path('create/', AccountCreateView.as_view(), name="create")
]