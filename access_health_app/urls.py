from django.urls import path, re_path
from . import views
from django.conf.urls import url

app_name = 'access_health_app'


urlpatterns = [

    path('post/create/', views.create_post, name='create_post'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:post_id>/comment/create/',
         views.comment_create, name='comment_create'),
    path('post/<int:post_id>/like/',
         views.like_post, name='like_post'),
    path('post/<int:post_id>/dislike/',
         views.dislike_post, name='dislike_post'),
     path('post/<int:post_id>/delete/',
         views.post_delete, name='post_delete'),
     path('post/<int:post_id>/detail/',
         views.post_detail, name='post_detail')
]