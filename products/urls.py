from django.urls import path
from . import views         #import views from home path


urlpatterns = [
    path('', views.all_products, name='products'),   
]