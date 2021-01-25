from django.urls import path
from . import views         #import views from home path


urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('<slug:slug>/remove/', views.remove_post, name='remove_post'),
]
