from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AccountUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']