from django import template
from .. import views

register = template.Library()

@register.inclusion_tag('starter_app/menu_in_blog.html', takes_context=True)
def total_posts(context):
    return {
        'posts': context['posts'],
        'selected_post': context['selected_post']
        }
