from accountapp.views import home
from django.urls import path

app_name = 'accountapp'

urlpatterns = [
    path('home/', home, name='home')
]