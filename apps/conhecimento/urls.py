from django.urls import path
from . import views

urlpatterns = [
    # Nova página inicial (Artigos)
    path('', views.artigos, name='artigos'),  # A página de artigos será a nova página inicial
    
    # Página que atualmente é o index (datatable)
    path('table-admin/', views.Index, name='table_admin'),  # Página que antes estava em '/'

    # Outras rotas...
    path('novo/', views.create_meumodelo, name='create_meumodelo'),
    path('editar/<int:pk>/', views.edit_meumodelo, name='edit_meumodelo'),
    path('excluir/<int:pk>/', views.delete_meumodelo, name='delete_meumodelo'),
    path('ver/<int:pk>/', views.view_meumodelo, name='view_meumodelo'),
    
    # Busca de artigos
    path('buscar-artigos/', views.buscar_artigos, name='buscar_artigos'),
    
    # Visualizar artigo
    path('ver-artigo/<int:pk>/', views.ver_artigo, name='ver_artigo'),
    
    # Editor de texto
    path('editar-texto/<int:pk>/', views.edit_texto, name='edit_texto'),
]
