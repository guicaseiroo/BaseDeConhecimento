from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('data-ajax-url/', views.data_ajax_url, name='data_ajax_url'),
    path('novo/', views.create_meumodelo, name='create_meumodelo'),  # Rota para criação de novo item
]
