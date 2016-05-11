from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/$', views.home, name='home'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.post, name='post'),
    ]
