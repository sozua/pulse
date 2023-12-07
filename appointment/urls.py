from django.urls import path

from . import views

urlpatterns = [
    path('', views.AppointmentListAPIView.as_view(), name="appointments"),
]