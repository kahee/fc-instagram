from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..models import Comment, Post
from ..forms import CommentModelForm


@login_required
def comment_create(request, pk):
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=Post.objects.get(pk=pk),
                author=request.user,
                content=form.cleaned_data['content']
            )

    return redirect('posts:post-list')
