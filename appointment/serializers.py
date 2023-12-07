from rest_framework import serializers

from appointment.models import Appointment
from professional.serializers import ProfessionalSerializer


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    professional = ProfessionalSerializer(many=False)

    class Meta:
        model = Appointment
        fields = ['id', 'professional', 'date', 'description']
