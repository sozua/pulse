
from django.test import TestCase

from professional.models import Professional


class TestProfessional(TestCase):
    def test_use_social_name_in_str(self):
        """ Social name should be used in str if available """
        professional = Professional(
			name='John Doe',
			social_name='Dr. Doe',
			specialty='Cardiology',
			registration_number='123456'
		)
        self.assertEqual(str(professional), 'Dr. Doe')