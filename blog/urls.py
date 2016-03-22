from django.conf.urls import url,include
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^api/$', views.PostList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    url(r'^add_comments/$', views.add_comments),
    url(r'^addPost/$', views.add_post, name='add_post'),
]
