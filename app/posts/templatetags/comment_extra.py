from django import template

register = template.Library()


@register.filter
def get_comment(value):
    post_comments = value.comments.filter(re_comment_id=None)
    return post_comments
