from django.contrib.auth.views import LoginView, LogoutView

from accountapp.views import home, AccountCreateView, AccountDetailView, AccountUpdateView
from django.urls import path

app_name = 'accountapp'

urlpatterns = [
    path('home/', home, name='home'),
    path('create/', AccountCreateView.as_view(), name="create"),
    path('login/', LoginView.as_view(template_name="accountapp/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
]