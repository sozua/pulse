from rest_framework import serializers

from appointment.models import Appointment
from professional.models import Professional
from professional.serializers import ProfessionalSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(queryset=Professional.objects.all())

    class Meta:
        model = Appointment
        fields = ['id', 'professional', 'date', 'description']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['professional'] = ProfessionalSerializer(instance.professional).data
        return representation