from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Usuário já existe')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('Usuário criado com sucesso')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            auth_login(request, user)
            return HttpResponse('Usuário autenticado')
        else:
            return HttpResponse('Email ou senha inválidos')