from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        if User.objects.get(pk=kwargs['pk']) == request.user:
            return func(*args, **kwargs)
        return HttpResponseForbidden()
    return decorated