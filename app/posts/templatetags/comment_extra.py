from django import template

register = template.Library()


@register.filter
def get_comment(value):
    post_comments = value.comments.filter(parent_comment=None)
    return post_comments
