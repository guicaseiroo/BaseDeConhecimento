from django.contrib import messages  # Para exibir mensagens de erro/sucesso
from django.contrib.auth.decorators import login_required
from django.core.exceptions import \
    ValidationError  # Para capturar erros de validação
from django.db import \
    IntegrityError  # Para capturar erros de integridade do banco de dados
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string

from .forms import MeuModeloForm
from .models import MeuModelo


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


@login_required
def create_meumodelo(request):
    if request.method == 'POST':
        form = MeuModeloForm(request.POST)

        if form.is_valid():
            # Salva os dados do formulário sem submeter ao banco de dados
            novo_item = form.save(commit=False)

            # Atribui o usuário autenticado como 'usuario_criador'
            novo_item.usuario_criador = request.user

            # Salva no banco de dados
            novo_item.save()

            # Redireciona para a página 'table_admin' após o salvamento
            return redirect('table_admin')
        else:
            print(f'Formulário inválido: {form.errors}')
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
            return redirect(
                'table_admin'
            )  # Redireciona para a página inicial após salvar
    else:
        form = MeuModeloForm(instance=meumodelo)

    return render(
        request, 'edit_meumodelo.html', {'form': form, 'item': meumodelo}
    )


@login_required
def delete_meumodelo(request, pk):
    meumodelo = get_object_or_404(MeuModelo, pk=pk)

    if request.method == 'POST':
        meumodelo.delete()
        return redirect('table_admin')

    return render(
        request, 'delete_meumodelo_confirm.html', {'item': meumodelo}
    )


@login_required
def view_meumodelo(request, pk):
    meumodelo = get_object_or_404(MeuModelo, pk=pk)
    return render(request, 'view_meumodelo.html', {'item': meumodelo})


# Novas views para a visão de artigos


def artigos(request):
    query = request.GET.get('busca', '')  # Captura o valor da searchbar
    if query:
        # Filtra artigos que contenham o termo de busca no título ou no texto
        artigos = MeuModelo.objects.filter(
            titulo__icontains=query
        ) | MeuModelo.objects.filter(texto__icontains=query)
    else:
        # Se não houver busca, retorna todos os artigos
        artigos = MeuModelo.objects.all()

    return render(
        request, 'artigos.html', {'artigos': artigos, 'query': query}
    )


def buscar_artigos(request):
    """Função que retorna artigos filtrados via HTMX"""
    query = request.GET.get('busca', '')
    if query:
        artigos = MeuModelo.objects.filter(
            titulo__icontains=query
        ) | MeuModelo.objects.filter(texto__icontains=query)
    else:
        artigos = MeuModelo.objects.all()

    return render(request, 'partials/artigos_cards.html', {'artigos': artigos})


def ver_artigo(request, pk):
    artigo = get_object_or_404(MeuModelo, pk=pk)
    return render(request, 'ver_artigos.html', {'artigo': artigo})
