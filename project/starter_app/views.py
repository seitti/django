import json, os
import dateutil.parser
from django.shortcuts import render
from config.settings.base import DJANGO_ROOT


def read_blog_homepage():
    json_path_posts = os.path.join(DJANGO_ROOT, 'starter_app', 'contents', 'posts_content.json')
    file_posts = open(json_path_posts, 'r')
    data_posts_json = json.load(file_posts)
    file_posts.close()

    for item in data_posts_json:
        item['date'] = dateutil.parser.parse(item['date'])

    return data_posts_json


def get_post_by_slug(slug):
    for item in home_data:
        if item['slug'] == slug:
            return item


def home(request):
    context_dict = {'selected_post': None,
                    'posts': home_data}
    return render(request, 'starter_app/home.html', context_dict)


def post(request, slug):
    context_dict = {'selected_post': get_post_by_slug(slug),
                    'posts': home_data}
    return render(request, 'starter_app/post.html', context_dict)


home_data = read_blog_homepage()
