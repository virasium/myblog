from django.urls import path
from .views import *

urlpatterns = [
    path('',PostsList.as_view(), name = 'posts_list_url'),
    path('post/create/',PostCreate.as_view(),name = 'post_create_url'),
    path('post/<slug>/',PostDetail.as_view(),name = 'post_detail_url'),
    path('post/<slug>/update/',PostUpdate.as_view(),name = 'post_update_url'),
    path('post/<slug>/delete/',PostDelete.as_view(),name = 'post_delete_url'),
    path('tags/',TagsList.as_view(),name = 'tags_list_url'),
    path('tag/create/',TagCreate.as_view(),name = 'tag_create_url'),
    path('tag/<slug>/',TagDetail.as_view(),name = 'tag_detail_url'),
    path('<id>/',comm_delete,name = 'comment_delete_url')
]
