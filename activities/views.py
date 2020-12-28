from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Activity, Interval
from .forms import ActivityForm, IntervalForm
from .tables import ActivityTable, IntervalTable, ActivityIntervalTable
from django_tables2 import RequestConfig
from .filters import IntervalFilter
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django_tables2 import SingleTableView


# Create your views here.
class ActivityListView(SingleTableView):
    model = Activity
    table_class = ActivityTable
    ordering = ["-date"]


class ActivityDetailView(DetailView):
    model = Activity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        intervals = Interval.objects.filter(activity=self.kwargs['pk'])
        context['table'] = ActivityIntervalTable(intervals)
        return context


class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm


class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm


class ActivityDeleteView(DeleteView):
    model = Activity
    success_url = reverse_lazy('index')


class IntervalListView(SingleTableView):
    model = Interval
    table_class = IntervalTable
    ordering = ["date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = IntervalFilter()
        context['filter'] = f
        return context
        
    def get_queryset(self):
        qs = self.model.objects.all()
        product_filtered_list = IntervalFilter(self.request.GET, queryset=qs)
        return product_filtered_list.qs


class IntervalDetailView(DetailView):
    model = Interval


class IntervalCreateView(CreateView):
    model = Interval
    form_class = IntervalForm
    template_name = "activities/activity_form.html"

    def form_valid(self, form):
        form.instance.activity = Activity.objects.get(pk=self.kwargs.get('pk'))
        return super(IntervalCreateView, self).form_valid(form)


class IntervalUpdateView(UpdateView):
    model = Interval
    form_class = IntervalForm
    template_name = "activities/activity_form.html"


class IntervalDeleteView(DeleteView):
    model = Interval
    success_url = reverse_lazy('index')
