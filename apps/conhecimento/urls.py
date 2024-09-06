from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('novo/', views.create_meumodelo, name='create_meumodelo'),
    path('editar/<int:pk>/', views.edit_meumodelo, name='edit_meumodelo'),
    path('excluir/<int:pk>/', views.delete_meumodelo, name='delete_meumodelo'),
    path('ver/<int:pk>/', views.view_meumodelo, name='view_meumodelo'),  # Adiciona URL para visualização
]
