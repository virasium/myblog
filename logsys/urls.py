from django.urls import path

from .views import *

urlpatterns = [
    path('login/',login_view,name = 'login_view_url'),
    path('logout/',logout_view,name = 'logout_view_url'),
    path('register/',register_view,name = 'register_view_url')
]
