from matrixApp.models import Post
from django import template
register=template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('HtmlFile/latest_posts123.html')
def show_letest_post():
    latest_posts=Post.objects.order_by('-publish')[:3]
    return {'latest_posts':latest_posts}

# from django.db.models import Count
# def get_most_commented_posts(count=5):
    