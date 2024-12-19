from django.urls import path
from . import views

urlatterns = [
    path('', views.post_list, name='post_list')
]
