from pets.models import Pet
from .serializers import PetSerializer
from rest_framework import generics

# Create your views here.


class PetListCreate(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
