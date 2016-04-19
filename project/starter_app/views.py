import json, os
from django.shortcuts import render
from config.settings.base import DJANGO_ROOT
from django.template.defaultfilters import slugify
# from .models import Message

json_path = os.path.join(DJANGO_ROOT, 'starter_app', 'contents', 'new_content.json')
f = open(json_path, 'r')
data = json.load(f)['my_string']
f.close()

json_path_posts = os.path.join(DJANGO_ROOT, 'starter_app', 'contents', 'posts.json')
file_posts = open(json_path_posts, 'r')
data_posts = json.load(file_posts)
file_posts.close()

for item in data_posts:
	data_posts[item]['slug'] = slugify(data_posts[item]['title'])


def home(request):
    # messages = Message.objects.order_by('order')
    # messages = ['Első', 'Második', 'Harmadik']
    # context_dict = {
        # 'messages': messages
    # }
    context_dict = {'messages' : data}
    return render(request, 'starter_app/home.html', context_dict)


def blog(request):
    posts = {'posts' : data_posts}
    return render(request, 'blog.html', posts)


def post(request):
	url_slug = str(request)[25:-3]
	for item in data_posts:
		if url_slug == data_posts[item]['slug']:
			posts = {'title' : data_posts[item]['title'],
					'date' : data_posts[item]['date'],
					'text' : data_posts[item]['text']}

	return render(request, 'post.html', posts)
