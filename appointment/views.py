from rest_framework.generics import ListCreateAPIView

from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer


class AppointmentListAPIView(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
