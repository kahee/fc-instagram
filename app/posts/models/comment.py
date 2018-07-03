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
    _author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    _content = models.CharField(
        max_length=255,
    )
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='comments',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment (post: {self.post.pk}, author:{self.author.username})'

    @property
    def author(self):
        if self.is_deleted:
            return None
        return self._author

    @property
    def content(self):
        if self.is_deleted:
            return '삭제된 댓글입니다.'
        return self._content

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
