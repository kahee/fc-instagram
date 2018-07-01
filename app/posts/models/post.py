import re

from django.conf import settings
from django.db import models

from ..models import HashTag


class Post(models.Model):
    PATTERN_HASHTAG = re.compile(r'#(?P<tag>\w+)')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post', blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        'posts.HashTag',
        blank=True
    )
    # 포스트를 좋아요 누른 유저
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PostLike',
        related_name='like_posts',
        blank=True,
    )

    class Meta:
        ordering = ['-pk']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for tag_name in re.findall(self.PATTERN_HASHTAG, self.content):
            tag, tag_create = HashTag.objects.get_or_create(name=tag_name)
            self.tags.add(tag)

    @property
    def content_html(self):
        return re.sub(self.PATTERN_HASHTAG, '<a href="/posts/tags/\g<tag>">#\g<tag></a>', self.content)

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
