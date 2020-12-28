from django.db import models
from django.urls import reverse
import time

type_choices = [
    ('', ""),
    ('Easy Run', "Easy Run"),
    ('Marathon Pace', "Marathon Pace"),
    ('Tempo', "Tempo"),
    ('Interval', "Interval"),
    ('Repetition', "Repetition"),
    ('Progressive', "Progressive"),
    ('Long Run', "Long Run"),
    ('Hill', "Hill"),
    ('Warm Up', 'Warm Up'),
    ('Cool Down', 'Cool Down'),
    ('Rest', 'Rest'),
    ('Jog', 'Jog'),
]

sport_choices = [
    ('Running', "Running"),
    ('Trail Running', "Trail Running"),
    ('Strength Training', "Strength Training"),
]

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    sport = models.CharField(max_length=75, choices=sport_choices, default="Running")
    type = models.CharField(max_length=75, choices=type_choices, blank=True)
    distance = models.FloatField(null=True, blank=True)
    duration = models.DurationField()
    heartrate = models.IntegerField(null=True, blank=True)
    elevation = models.IntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("activity", kwargs={"pk": self.pk})
    

    def pace(self):
        return time.strftime('%M:%S', time.gmtime((self.duration / self.distance).seconds)) + " /km"

class Interval(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    type = models.CharField(max_length=75, choices=type_choices)
    distance = models.FloatField(null=True, blank=True)
    duration = models.DurationField()
    heartrate = models.IntegerField(null=True, blank=True)
    elevation = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("activity", kwargs={"pk": self.pk})

    def pace(self):
        return time.strftime('%M:%S', time.gmtime((self.duration / self.distance).seconds)) + " /km"



