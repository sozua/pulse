import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer
from professional.models import Professional


class AppointmentViewsetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.professional = Professional.objects.create(name='Test Professional 1')
        self.professional2 = Professional.objects.create(name='Test Professional 2')
        self.appointment = Appointment.objects.create(
            date='2022-01-01 12:00:00',
            description='Checkup',
            professional=self.professional
        )
        self.appointment2 = Appointment.objects.create(
            date='2022-01-02 12:00:00',
            description='Checkup',
            professional=self.professional
        )
        self.appointment3 = Appointment.objects.create(
            date='2022-01-03 12:00:00',
            description='Checkup',
            professional=self.professional2
        )
        self.valid_payload = {
            'date': '2022-01-03 12:00:00',
            'description': 'Checkup',
            'professional': str(self.professional2.pk)
        }
        self.invalid_payload = {
            'date': 'invalid date'
        }

    def test_list_appointments(self):
        response = self.client.get(reverse("appointments"))
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        response_data = response.json().get('results', [])
        self.assertEqual(response_data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_appointments_by_professional_id(self):
        professional_id = self.professional.pk
        response = self.client.get(reverse("appointments"), {'professional_id': professional_id})
        appointments = Appointment.objects.filter(professional__id=professional_id)
        serializer = AppointmentSerializer(appointments, many=True)
        response_data = response.json().get('results', [])
        self.assertEqual(response_data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_appointment(self):
        response = self.client.post(
            reverse("appointments"),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_appointment(self):
        response = self.client.post(
            reverse("appointments"),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_valid_appointment(self):
        response = self.client.get(reverse("appointment", kwargs={'pk': self.appointment.pk}))
        appointment = Appointment.objects.get(pk=self.appointment.pk)
        serializer = AppointmentSerializer(appointment)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_invalid_appointment(self):
        response = self.client.get(reverse("appointment", kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.get(reverse("appointment", kwargs={
            'pk': 'dd277de0-5ae7-4133-8060-acd93f0288e7'
        }))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_appointment(self):
        response = self.client.put(
            reverse("appointment", kwargs={'pk': self.appointment.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        appointment = Appointment.objects.get(pk=self.appointment.pk)
        serializer = AppointmentSerializer(appointment)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_appointment(self):
        response = self.client.put(
            reverse("appointment", kwargs={'pk': self.appointment.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_appointment(self):
        response = self.client.delete(reverse("appointment", kwargs={'pk': self.appointment.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_appointment(self):
        response = self.client.delete(reverse("appointment", kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)