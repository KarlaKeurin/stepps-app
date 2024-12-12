from django.urls import path
from dashboard.views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    # dashboard:login
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
