from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^posts/$', views.blog, name='blog'),
    # url(r'^blog/post/$', views.post, name='post'),
    # url(r'^posts/.+/$', views.post, name='post'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.post, name='post'),
    ]
