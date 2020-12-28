import django_tables2 as tables
from .models import Activity, Interval
from django_tables2.utils import A

class DistanceColumn(tables.Column):
    def render(self, record):
        return f"{record.distance} km"


class ActivityTable(tables.Table):
    title = tables.LinkColumn("activity", args=[A("pk")])
    distance = DistanceColumn()
    class Meta:
        model = Activity
        template_name = "django_tables2/bootstrap.html"
        fields = ("title", "date", "sport", "type", "distance", "duration", "pace", "heartrate", "elevation")

class ActivityIntervalTable(tables.Table):
    type = tables.LinkColumn("interval", args=[A("pk")])
    distance = DistanceColumn()
    class Meta:
        model = Interval
        template_name = "django_tables2/bootstrap.html"
        fields = ("type", "distance", "duration", "pace", "heartrate", "elevation")

class IntervalTable(tables.Table):
    distance = DistanceColumn()
    class Meta:
        model = Interval
        template_name = "django_tables2/bootstrap.html"
        fields = ("activity", "activity.date", "type", "distance", "duration", "pace", "heartrate", "elevation")