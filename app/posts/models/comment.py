from django.conf import settings
from django.db import models


# 하나의 포스트에 여러개의 댓글을 달 수 있다.
#  one_to_many 관계 대댓글의 경우 한 댓글에 여러개의 댓글 리플이 달리 수 잇음 1:다... (
class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_by_user'
    )
    content = models.CharField(
        max_length=255,
    )
    re_comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='re_comments',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
