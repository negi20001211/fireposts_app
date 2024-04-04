from django.urls import path
from posts import views

urlpatterns = [
    path('posts_top/',views.posts_top,name="posts_top"),
    path('post_new/',views.post_new,name='post_new'),
    path('<int:post_id>/',views.post_detail,name='post_detail'),
    path('<int:post_id>/edit/',views.post_edit,name='post_edit'),
    
]
