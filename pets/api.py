from .models import Pet, Report
from rest_framework import viewsets, permissions
from .serializers import PetSerializer

#Pet Viewset
class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PetSerializer