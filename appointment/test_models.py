from django.db import IntegrityError
from django.test import TestCase

from appointment.models import Appointment


class TestAppointment(TestCase):
    def test_require_professional(self):
        with self.assertRaises(IntegrityError):
            Appointment(
				date='2021-01-01 12:00:00',
				description='Checkup'
			).save()
