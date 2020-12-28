from django.contrib import admin
from .models import Activity, Interval

# Register your models here.

class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'sport', 'type', 'distance', 'duration', 'heartrate', 'comment', 'elevation']

class IntervalsAdmin(admin.ModelAdmin):
    list_display = ['activity', 'type', 'distance', 'duration', 'heartrate', 'elevation']

admin.site.register(Activity, ActivitiesAdmin)
admin.site.register(Interval, IntervalsAdmin)