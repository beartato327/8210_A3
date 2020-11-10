from django.urls import path
from . import views
from .views import(
    PetListView,
    PetUpdateView,
    PetDetailView,
    PetCreateView
)
#app_name = 'pet'
urlpatterns = [
    path('<uuid:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('<uuid:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),
    path('add/', PetCreateView.as_view(), name='pet_new'),
    path('', PetListView.as_view(), name='pet_list'),
]