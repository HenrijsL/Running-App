from django.forms import ModelForm
from django import forms
from .models import type_choices, sport_choices, Activity, Interval
import datetime

class ActivityForm(ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.datetime.now())
    class Meta:
        model = Activity
        fields = ['title', 'date', 'sport', 'type', 'distance', 'duration', 'heartrate', 'elevation', 'comment']

class IntervalForm(ModelForm):
    class Meta:
        model = Interval
        fields = ['type', 'distance', 'duration', 'heartrate', 'elevation']

