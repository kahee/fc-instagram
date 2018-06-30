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


@login_required
def re_comment_create(request, pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=pk)
        form = CommentModelForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=Post.objects.get(pk=comment.post.pk),
                author=request.user,
                content=form.cleaned_data['content'],
                re_comment=comment,
            )
    return redirect('posts:post-list')
