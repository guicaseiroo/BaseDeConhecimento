from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MeuModelo

@login_required
def Index(request):
    if request.method == "GET":
        items = MeuModelo.objects.all()
        return render(request, 'index.html', {'items': items})

def data_ajax_url(request):
    data = list(MeuModelo.objects.values(
        'id', 'titulo', 'categorias', 'validade', 
        'usuario_criador__username', 'data_created', 'data_updated'
    ))

    return JsonResponse({
        'data': data
    })