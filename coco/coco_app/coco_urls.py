from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("time_logger/<int:time_id>", views.time_logger, name="time_logger"),
    path("time_overview", views.time_overview, name="time_overview"),
]