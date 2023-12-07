import uuid

from django.db import models


class Professional(models.Model):
    """ Health professional model """
    id=models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
    name = models.CharField(max_length=100)
    social_name = models.CharField(max_length=100, blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    registration_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        if self.social_name:
            return str(self.social_name)
        return str(self.name)