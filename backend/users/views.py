from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, logout, login as auth_login
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.authtoken.models import Token

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
        user.is_active = True
        user.save()

        return HttpResponse('Usuário criado com sucesso')
        
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.filter(email=email).first()

            if user and user.check_password(password):
                auth_login(request, user)
                user_data = UserSerializer(user).data
                return JsonResponse(user_data, status=200)
            else:
                return JsonResponse({'error': 'Email ou senha inválidos'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato de dados inválido'}, status=400)
