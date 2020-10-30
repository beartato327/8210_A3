from rest_framework import routers
from .api import PetViewSet

router = routers.DefaultRouter()
router.register('api/pets', PetViewSet, 'pets')

urlpatterns = router.urls