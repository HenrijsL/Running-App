import django_filters
from .models import Interval

class IntervalFilter(django_filters.FilterSet):
    class Meta:
        model = Interval
        fields = ["type"]
