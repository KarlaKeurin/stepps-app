from django.urls import path
from users.views import login
from users.views import cadastro

app_name = 'users'

urlpatterns = [
    # users:login
    path('', login, name='login'),
    # users:cadastro
    path('cadastro/', cadastro, name='cadastro'),
]
