from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post', blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 포스트를 좋아요 누른 유저
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PostLike',
        related_name='like_posts',
        blank=True,
    )

    class Meta:
        ordering = ['-pk']

    def toggle_like_user(self, user):
        """
        like_uesr에 주어진 user가 없는 경우,like_user에 추가
        :param user:
        :return:
        """
        like, like_created = self.like_user_info_list.get_or_create(user=user)
        if not like_created:
            like.delete()
        return like_created
