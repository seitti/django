import json, os
from django.shortcuts import render
from config.settings.base import DJANGO_ROOT
from dateutil.parser import parse


def read_blog_homepage():
    json_path_posts = os.path.join(DJANGO_ROOT, 'starter_app', 'contents', 'posts_content.json')
    file_posts = open(json_path_posts, 'r')
    data_posts_json = json.load(file_posts)
    file_posts.close()

    for item in data_posts_json:
        item['date'] = parse(item['date'])

    return data_posts_json


def get_post_by_slug(slug):
    for item in homepage:
        if item['slug'] == slug:
            select_post = item
    return select_post


def home(request):
    context_dict = {'posts' : homepage}
    return render(request, 'starter_app/home.html', context_dict)


def post(request, slug):
    context_dict = {'selected_post' : get_post_by_slug(slug), 'posts' : homepage}
    return render(request, 'starter_app/post.html', context_dict)


homepage = read_blog_homepage()
