import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from professional.models import Professional
from professional.serializers import ProfessionalSerializer


class ProfessionalViewsetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.professional1 = Professional.objects.create(name='Test Professional 1')
        self.professional2 = Professional.objects.create(name='Test Professional 2')
        self.valid_payload = {
            'name': 'Test Professional 3'
        }
        self.invalid_payload = {
            'name': '',
        }

    def test_list_professionals(self):
        response = self.client.get(reverse("professionals"))
        professionals = Professional.objects.all()
        serializer = ProfessionalSerializer(professionals, many=True)
        response_data = response.json().get('results', [])
        self.assertEqual(response_data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_professional(self):
        response = self.client.post(
            reverse("professionals"),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_professional(self):
        response = self.client.post(
            reverse("professionals"),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_valid_professional(self):
        response = self.client.get(reverse("professional", kwargs={'pk': self.professional1.pk}))
        professional = Professional.objects.get(pk=self.professional1.pk)
        serializer = ProfessionalSerializer(professional)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_invalid_professional(self):
        response = self.client.get(reverse("professional", kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.get(reverse("professional", kwargs={
            'pk': 'dd277de0-5ae7-4133-8060-acd93f0288e7'
        }))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_professional(self):
        response = self.client.put(
            reverse("professional", kwargs={'pk': self.professional1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        professional = Professional.objects.get(pk=self.professional1.pk)
        serializer = ProfessionalSerializer(professional)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_professional(self):
        response = self.client.put(
            reverse("professional", kwargs={'pk': self.professional1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_professional(self):
        response = self.client.delete(reverse("professional", kwargs={'pk': self.professional1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_professional(self):
        response = self.client.delete(reverse("professional", kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
