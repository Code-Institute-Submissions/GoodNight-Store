from django.urls import path
from . import views         #import views from home path


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product')
]
