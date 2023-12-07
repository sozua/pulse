
from django.db.utils import IntegrityError
from django.test import TestCase

from professional.models import Professional


class TestProfessional(TestCase):
    def test_use_social_name_in_str(self):
        professional = Professional(
            name='John Doe',
            social_name='Dr. Doe',
            specialty='Cardiology',
            registration_number='123456'
        )
        self.assertEqual(str(professional), 'Dr. Doe')

    def test_unique_registration_number(self):
        professional = Professional(
            name='John Doe',
            social_name='Dr. Doe',
            specialty='Cardiology',
            registration_number='123456'
        )
        professional.save()
        professional2 = Professional(
            name='John Doe',
            social_name='Dr. Doe',
            specialty='Cardiology',
            registration_number='123456'
        )
        with self.assertRaises(Exception) as raised:
            professional2.save()
        self.assertEqual(IntegrityError, type(raised.exception))
