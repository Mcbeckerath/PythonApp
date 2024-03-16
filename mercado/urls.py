from django.urls import path

from mercado import views

urlpatterns = [
   
    path('', views.home, name='home'),
]