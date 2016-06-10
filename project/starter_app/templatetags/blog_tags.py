from django import template
from ..views import home_data

register = template.Library()

@register.inclusion_tag('starter_app/menu_in_blog.html')
def generate_menu(selected_post=None):
    return {
        'posts': home_data,
        'selected_post': selected_post
        }
