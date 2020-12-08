from django.db import models
import time

# Create your models here.
class Activitie(models.Model):
    type_choices = [
        ('easy run', "Easy Run"),
        ('marathon pace', "Marathon Pace"),
        ('tempo', "Tempo"),
        ('interval', "Interval"),
        ('repetition', "Repetition"),
        ('progressive', "Progressive"),
    ]
    title = models.CharField(max_length=150)
    date = models.DateField()
    type = models.CharField(max_length=75, choices=type_choices)
    distance = models.FloatField()
    time = models.DurationField()
    heartrate = models.IntegerField(blank=True)
    comment = models.TextField(blank=True)
    
    def pace(self):
        return time.strftime('%M:%S', time.gmtime((self.time / self.distance).seconds))



