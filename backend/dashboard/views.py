from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Dashboard
from .serializers import DashboardSerializer

class DashboardView(APIView):
    def get(self, request):
        dashboard = Dashboard.objects.first()

        if not dashboard:
            return Response({'message': 'No data available'}, status=404)
        
        daily_data = dashboard.calculate_daily_today()
        alerts_per_hour = dashboard.calculate_alerts_per_hour()

        serializer = DashboardSerializer(dashboard)
        serialized_data = dict(serializer.data)

        serialized_data.update({
            'daily_data': daily_data,
            'alerts_per_hour': alerts_per_hour
        })

        return Response(serialized_data)




# data = {
#     'total_people_passed': daily_data['total_people_passed'],
#     'current_people': daily_data['current_people'],
#     'total_accidents': daily_data['total_accidents'],
#     'total_events': daily_data['total_events'],
#     'alerts_per_hour': alerts_per_hour,
# }