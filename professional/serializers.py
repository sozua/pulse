from rest_framework import serializers

from professional.models import Professional


class ProfessionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professional
        fields = ['id', 'name', 'social_name', 'specialty', 'registration_number']
