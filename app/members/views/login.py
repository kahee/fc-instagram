from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import redirect, render

from ..forms import FacebookModelForm

User = get_user_model()

__all__ = (
    'facebook_login',
)


def facebook_login(request):
    code = request.GET.get('code')
    user = authenticate(request, code=code)

    if user:
        # 페이스북으로 로그인시 이미 유저가 있는 경우
        login(request,user)
        return redirect('index')

    if request.method == 'POST':
        form = FacebookModelForm(request.POST)
        print('sdf')

        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(request, code=code, extra_info=form.cleaned_data)
            login(request, user)
            return redirect('index')

    else:
        form = FacebookModelForm()

    context = {
        'form': form,
    }

    return render(request, 'members/facebook_login.html', context)
