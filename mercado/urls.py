from django.urls import path

from mercado import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('produto/<id_produto>', views.produto, name='produto'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('form_produto/', views.form_produto, name ='form_produto'),
    path('form_usuario/', views.form_usuario, name='form_usuario')
   ]