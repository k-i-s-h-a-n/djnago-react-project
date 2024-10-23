from django.urls import path,include
from ecomapp import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    
]
