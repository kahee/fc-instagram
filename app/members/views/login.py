import requests
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import redirect

User = get_user_model()

__all__ = (
    'facebook_login',
)


def facebook_login(request):
    code = request.GET.get('code')
    user = authenticate(request,code=code)

    if user is not None:
        login(request,user)

    return redirect('members:login')