import uuid

from django.db import models

from professional.models import Professional


class Appointment(models.Model):
    """ Appointment model """
    id=models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
    professional = models.ForeignKey(
		Professional,
		on_delete=models.CASCADE,
		related_name='appointments'
	)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.professional} - {self.date}'
