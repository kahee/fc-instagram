from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..forms import CommentModelForm


@login_required
def comment_create(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CommentModelForm()

    context = {
        'comment_form': form,
    }

    return render(request, 'post/post_list.html', context)
