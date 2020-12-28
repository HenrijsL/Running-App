from django.urls import path
from .views import (ActivityListView, ActivityCreateView, ActivityDetailView, ActivityUpdateView, 
                    ActivityDeleteView, IntervalListView, IntervalDetailView, 
                    IntervalUpdateView, IntervalCreateView, IntervalDeleteView)
from . import views

urlpatterns = [
    path('', ActivityListView.as_view(), name='index'),
    path('create', ActivityCreateView.as_view(), name="create"),
    path('<int:pk>', ActivityDetailView.as_view(), name="activity"),
    path('<int:pk>/delete', ActivityDeleteView.as_view(), name="delete"),
    path('<int:pk>/update', ActivityUpdateView.as_view(), name="update"),
    path('intervals', IntervalListView.as_view(), name="intervals"),
    path('intervals/create/<int:pk>', IntervalCreateView.as_view(), name="interval-create"),
    path('intervals/<int:pk>', IntervalDetailView.as_view(), name="interval"),
    path('intervals/<int:pk>/update',IntervalUpdateView.as_view(), name="interval-update"),
    path('intervals/<int:pk>/delete',IntervalDeleteView.as_view(), name="interval-delete")
]
