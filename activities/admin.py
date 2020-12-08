from django.contrib import admin
from .models import Activitie

# Register your models here.

class ActivitieAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'type', 'distance', 'time', 'heartrate', 'comment']

admin.site.register(Activitie, ActivitieAdmin)