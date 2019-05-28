from django.urls import path
from .views import *

urlpatterns = [
    path('',PostsList.as_view(), name = 'posts_list_url'),
    path('post/<slug>/',PostDetail.as_view(),name = 'post_detail_url'),
    path('tags/',TagsList.as_view(),name = 'tags_list_url'),
    path('tag/<slug>/',TagDetail.as_view(),name = 'tag_detail_url')
]
