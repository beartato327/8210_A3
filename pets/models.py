from django.db import models
from users.models import CustomUser
from django.urls import reverse
from django.conf import settings
import uuid

# Create your models here.
class Pet(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE )
    pet_type = models.CharField(max_length=200, blank=False)
    pet_name = models.CharField(max_length=200, blank=False)
    pet_age = models.PositiveIntegerField()
    pet_breed = models.CharField(max_length=200)

    def __str__(self):
        return self.pet_name

    def get_absolute_url(self):
        return reverse('pet_detail', args=[str(self.id)])

class Report(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='pets')
    reportName = models.CharField(max_length=200)
    reportType = models.CharField(max_length=200)
    reportDetails = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reportType

    def get_absolute_url(self):
        return reverse('report_detail', args=[str(self.pet_id)])
    