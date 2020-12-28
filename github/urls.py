
from django.urls import path
from .views import *


urlpatterns = [
    path('' , index , name="index"),
    path('get/', get_user_details  , name="index"),
    path('followers/' , get_user_followers , name="get_user_followers"),
    path('create/', create_new_repository , name="create_new_repository"),
    path('update/' , update_repository_description , name="update_repository_description"),
    path('highest/' , get_highest_follower , name="get_highest_follower")
]
