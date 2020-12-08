from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Activitie
from .forms import AddForm

# Create your views here.
def index(request):
    return render(request, "activities/index.html", {"activities": Activitie.objects.all()})

def add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            type = form.cleaned_data['type']
            distance = form.cleaned_data['distance']
            time = form.cleaned_data['time']
            heartrate = form.cleaned_data['heartrate']
            comment = form.cleaned_data['comment']
            Activitie.objects.create(title = title, date = date, type = type, distance = distance, time = time, heartrate = heartrate, comment = comment)
            return HttpResponseRedirect(reverse("index"))
    form = AddForm()
    return render(request, "activities/add.html", {"form": form})