import datetime

from django.conf import settings
from django.db import models


class PostLike(models.Model):
    # Post와 User와의 MTM모델
    post = models.ForeignKey(
        'Post',
        related_name='like_user_info_list',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='like_post_info_list',
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            ('post', 'user'),
        )

    def __str__(self):
        return 'PostLike (User:{user}, Post:{post}, Created:{created})'.format(
            artist=self.post,
            user=self.user.username,
            created=datetime.strftime(self.created_date, '%Y.%m.%d'),
        )
