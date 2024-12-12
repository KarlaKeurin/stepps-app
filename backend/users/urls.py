from django.urls import path
from users.views import login
from users.views import cadastro
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # users:login
    path('', login, name='login'),
    # users:cadastro
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
