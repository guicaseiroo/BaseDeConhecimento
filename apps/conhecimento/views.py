from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import MeuModelo
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

