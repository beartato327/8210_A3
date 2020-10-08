from django.db import models
from users.models import CustomUser
import uuid

# Create your models here.
class Pet(models.Model):
    PET_TYPE = (
        ('DOG', 'Dog'),
        ('CAT', 'Cat')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE )
    pet_type = models.CharField(choices=PET_TYPE, max_length=3,verbose_name='type of pet',null=False)
    pet_name = models.CharField(max_length=200, blank=False)
    pet_age = models.IntegerField(null=False)
    pet_breed = models.CharField(max_length=200)

    def __str__(self):
        return self.pet_name

class Report(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='pets')
    reportName = models.CharField(max_length=200)
    reportType = models.CharField(max_length=100)
    reportDetails = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reportType
    