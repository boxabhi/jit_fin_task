
from django.urls import path
from .views import *


urlpatterns = [
    path('', index  , name="index"),
    path('api/' , get_user_details , name="get_user_details")
]
