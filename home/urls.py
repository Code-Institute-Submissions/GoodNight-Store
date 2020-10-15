from django.contrib import admin
from django.urls import path
from . import views         #import views from home path


urlpatterns = [
    path('', views.index, name='home'),     # add index from views to the path named home
]
