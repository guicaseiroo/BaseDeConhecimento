from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .models import MeuModelo
from .forms import MeuModeloForm


@login_required
def Index(request):
    if request.method == 'GET':
        items = MeuModelo.objects.all()
        return render(request, 'index.html', {'items': items})


def data_ajax_url(request):
    data = list(
        MeuModelo.objects.values(
            'id',
            'titulo',
            'categorias',
            'validade',
            'usuario_criador__username',
            'data_created',
            'data_updated',
        )
    )
    return JsonResponse({'data': data})


def create_meumodelo(request):
    if request.method == 'POST':
        form = MeuModeloForm(request.POST)
        if form.is_valid():
            novo_item = form.save(commit=False)
            novo_item.usuario_criador = request.user  # Definindo o criador como o usuário logado
            novo_item.save()
            return redirect('index')  # Redireciona para a página principal após criação
    else:
        form = MeuModeloForm()
    return render(request, 'create_meumodelo.html', {'form': form})


@login_required
def edit_meumodelo(request, pk):
    meumodelo = get_object_or_404(MeuModelo, pk=pk)

    if request.method == 'POST':
        form = MeuModeloForm(request.POST, instance=meumodelo)
        if form.is_valid():
            form.save()  # Salva o formulário, atualizando o item
            return redirect('index')  # Redireciona para a página inicial após salvar
    else:
        form = MeuModeloForm(instance=meumodelo)
    
    return render(request, 'edit_meumodelo.html', {'form': form, 'item': meumodelo})


@login_required
def delete_meumodelo(request, pk):
    meumodelo = get_object_or_404(MeuModelo, pk=pk)

    if request.method == "POST":
        meumodelo.delete()
        return redirect('index')

    return render(request, 'delete_meumodelo_confirm.html', {'item': meumodelo})


@login_required
def view_meumodelo(request, pk):
    meumodelo = get_object_or_404(MeuModelo, pk=pk)
    return render(request, 'view_meumodelo.html', {'item': meumodelo})


# Novas views para a visão de artigos

def artigos(request):
    # Renderiza a página principal de visualização dos artigos
    artigos = MeuModelo.objects.all()
    return render(request, 'artigos.html', {'artigos': artigos})


def buscar_artigos(request):
    query = request.GET.get('query', '')
    artigos = MeuModelo.objects.filter(titulo__icontains=query) | MeuModelo.objects.filter(texto__icontains=query)
    
    html = render_to_string('partials/artigos_cards.html', {'artigos': artigos})
    
    return JsonResponse({'html': html})


def ver_artigo(request, pk):
    artigo = get_object_or_404(MeuModelo, pk=pk)
    return render(request, 'ver_artigos.html', {'artigo': artigo})
