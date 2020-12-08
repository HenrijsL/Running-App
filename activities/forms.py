from django import forms
from .models import Activitie
import datetime

class AddForm(forms.Form):
    title = forms.CharField(label="Title", max_length=150)
    date = forms.DateField(label="Date", initial=datetime.datetime.now(), widget=forms.SelectDateWidget)
    type = forms.ChoiceField(label="Type", choices=Activitie.type_choices)
    distance = forms.FloatField(label="Distance", min_value=0)
    time = forms.DurationField(label="Duration")
    heartrate = forms.IntegerField(label="Heart Rate", min_value=0, required=False)
    comment = forms.CharField(label="Comment", widget=forms.Textarea, required=False)

