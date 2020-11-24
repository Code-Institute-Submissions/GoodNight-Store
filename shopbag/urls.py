from django.urls import path
from . import views         #import views from home path


urlpatterns = [
        # add index from views to the path named home
    path('', views.shopbag, name='shopbag'),     

]
