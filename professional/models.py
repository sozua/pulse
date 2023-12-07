import uuid

from django.db import models


class Professional(models.Model):
    id=models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
    name = models.CharField(max_length=100)
    social_name = models.CharField(max_length=100, blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    registration_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        if self.social_name:
            return str(self.social_name)
        return str(self.name)
