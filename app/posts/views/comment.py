from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from ..models import Comment, Post
from ..forms import CommentModelForm


@require_POST
@login_required
def comment_create(request, post_pk, comment_pk=None):
    form = CommentModelForm(request.POST)
    parent_comment = get_object_or_404(Comment, pk=comment_pk) if comment_pk else None
    if form.is_valid():
        Comment.objects.create(
            post=Post.objects.get(pk=post_pk),
            _author=request.user,
            _content=form.cleaned_data['_content'],
            parent_comment=parent_comment,
        )
    return redirect('posts:post-list')
