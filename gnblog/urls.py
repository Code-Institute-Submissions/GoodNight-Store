from django.urls import path
from . import views         #import views from home path


urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.add_post, name='add_post'),
]
