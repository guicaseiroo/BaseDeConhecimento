# from rolepermissions.decorators  import has_permission_decorator
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Users


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_validation = auth.authenticate(
            username=username, password=password
        )

        if not user_validation:
            return render(
                request,
                'login.html',
                {'messages': 'Usuário e/ou senha incorretos'},
            )

        auth.login(request, user_validation)
        return redirect(reverse('index'))


@login_required
def logout_sys(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('index'))
