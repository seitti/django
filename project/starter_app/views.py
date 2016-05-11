import json, os

from django.shortcuts import render
from config.settings.base import DJANGO_ROOT
from dateutil.parser import parse


def publish_date(json_date):
    date = parse(json_date)
    return date


def read_home_json():
    json_path = os.path.join(DJANGO_ROOT, 'starter_app', 'contents', 'new_content.json')
    f = open(json_path, 'r')
    home_data_json = json.load(f)['my_string']
    f.close()
    return home_data_json


def read_blog_json():
    json_path_posts = os.path.join(DJANGO_ROOT, 'starter_app', 'contents', 'posts.json')
    file_posts = open(json_path_posts, 'r')
    data_posts_json = json.load(file_posts)
    file_posts.close()

    for item in data_posts_json:
        item['date'] = publish_date(item['date'])

    return data_posts_json


def post_slug(slug):
    for item in data_posts:
        if item['slug'] == slug:
            select_post = item
    return select_post


def home(request):
    context_dict = {'messages' : home_data}
    return render(request, 'starter_app/home.html', context_dict)


def blog(request):
    context_dict = {'posts' : data_posts}
    return render(request, 'blog.html', context_dict)


def post(request, slug):
    context_dict = post_slug(slug)
    return render(request, 'post.html', context_dict)

home_data = read_home_json()
data_posts = read_blog_json()
