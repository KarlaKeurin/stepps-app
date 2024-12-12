from django.urls import path
from dashboard.views import DashboardView
from django.contrib.auth import views as auth_views

app_name = 'dashboard'

urlpatterns = [
    # dashboard:login
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
