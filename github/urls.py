
from django.urls import path
from .views import *


urlpatterns = [
    path('', get_user_details  , name="index"),
    path('api/' , get_user_details , name="get_user_details"),
    path('create', create_new_repository , name="create_new_repository"),
    path('update/' , update_repository_description , name="update_repository_description")
]
