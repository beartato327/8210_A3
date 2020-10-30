from rest_framework import serializers
from .models import Pet, Report

#Pet Serializer
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'