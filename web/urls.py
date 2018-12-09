from django.urls import re_path, path

from web.views import *

urlpatterns = [

   # path('posts/<str:post_type>', posts),
   # path('favorites', favorites),
   # path('like_favorite/<int:id>', like_favorite),
   # path('add_favorite/<str:quote>', add_favorite),
   # re_path('login',login),
   # re_path('register',register),
    path('login', login),
    path('userregister', userregister),
    path('user',user),
    path('user1',user1),
    path('userlogin',userlogin),
    path('usertable',usertable),
    
    path('register', register),
    path('home', home),
    re_path('', index),
]