from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog/$', views.blog, name='blog'),
    # url(r'^blog/post/$', views.post, name='post'),
    url(r'^blog/.+/$', views.post, name='post'),
    ]
