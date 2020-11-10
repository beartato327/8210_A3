from pets.models import Pet
from rest_framework import viewsets, permissions
from .serializers import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PetSerializer

    def get_queryset(self):
        return self.request.user.pets.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)