from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

User = get_user_model()


@require_POST
@login_required
def follow_toggle(request, user_pk):
    """
    * GET요청은 처리하지 않음
    * 로그인 된 상태에서만 작동

    POST요청일 때
        1. request.POST로 'user_pk'값을 전달받음
            pk가 user_pk인 User를 user에 할당
        2. request.user의
    :param request:
    :return:
    """

    to_user = User.objects.get(pk=user_pk)
    request.user.follow(to_user)
    return redirect('posts:post-list')


@require_POST
@login_required
def unfollow_toggle(request, user_pk):
    to_user = User.objects.get(pk=user_pk)
    request.user.unfollow(to_user)
    return redirect('posts:post-list')


@require_POST
@login_required
def block_toggle(request, user_pk):
    to_user = User.objects.get(pk=user_pk)
    request.user.block_users(to_user)
    return redirect('posts:post-list')
