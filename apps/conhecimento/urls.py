from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('novo/', views.create_meumodelo, name='create_meumodelo'),
    path('editar/<int:pk>/', views.edit_meumodelo, name='edit_meumodelo'),
    path('excluir/<int:pk>/', views.delete_meumodelo, name='delete_meumodelo'),
    path('ver/<int:pk>/', views.view_meumodelo, name='view_meumodelo'),

    # URLs para os artigos
    path('artigos/', views.artigos, name='artigos'),  # Página com os cards de artigos
    path('buscar-artigos/', views.buscar_artigos, name='buscar_artigos'),  # Busca dinâmica via HTMX
    path('ver-artigo/<int:pk>/', views.ver_artigo, name='ver_artigo'),  # Página completa de visualização do artigo
]
