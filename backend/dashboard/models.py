from django.db import models
from django.utils import timezone
from django.db.models import Avg
from django.db.models import Sum

class Dashboard(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    total_people_passed = models.IntegerField(default=0)
    current_people = models.IntegerField(default=0)
    total_accidents = models.IntegerField(default=0)
    total_events = models.IntegerField(default=0)
    alerts_per_hour = models.JSONField(default=dict)  # {"08:00": 2, "09:00": 3}

    def calculate_daily_today(self):
        today = timezone.now().date()
        daily_data = Dashboard.objects.filter(created_at__date=today).aggregate(
            total_people_passed=Sum('total_people_passed'),
            current_people=Sum('current_people'),
            total_accidents=Sum('total_accidents'),
            total_events=Sum('total_events'),
        )
        return daily_data


    def calculate_alerts_per_hour(self):
        today = timezone.now().date()
        alerts = Dashboard.objects.filter(created_at__date=today).values('created_at__hour').annotate(total_accidents=Sum('total_accidents'))
        alerts_per_hour = {f"{hour['created_at__hour']:02d}:00": hour['total_accidents'] for hour in alerts}
        return alerts_per_hour

    def __str__(self):
        average_alerts = self.calculate_alerts_per_hour()
        return f"Dashboard: {self.total_people_passed} people passed, {self.current_people} people currently, {self.total_accidents} accidents, {self.total_events} events, average alerts per hour: {average_alerts}"