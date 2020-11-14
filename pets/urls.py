from django.urls import path
from . import views
from .views import(
    PetListView,
    PetUpdateView,
    PetDetailView,
    PetCreateView,
    ReportListView,
    ReportCreateView,
    ReportDetailView,
)
#app_name = 'pet'
urlpatterns = [
    path('<uuid:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('<uuid:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),
    path('add/', PetCreateView.as_view(), name='pet_new'),
    path('<uuid:pk>/report_list', ReportListView.as_view(), name='report_list'),
    path('<uuid:pk>/add_report/', ReportCreateView.as_view(), name='report_new'),
    path('<uuid:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('', PetListView.as_view(), name='pet_list'),
]