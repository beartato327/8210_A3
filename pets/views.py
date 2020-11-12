from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .forms import PetForm 
from .models import Pet, Report

class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    template_name = 'pet/pet_list.html'

class PetDetailView(LoginRequiredMixin,DetailView):
    model = Pet
    template_name = 'pet/pet_detail.html'
    login_url='login'

class PetUpdateView(LoginRequiredMixin,UpdateView):
    model = Pet
    fields = ('pet_name', 'pet_type', 'pet_age','pet_breed')
    template_name = 'pet/pet_edit.html'

class PetCreateView(LoginRequiredMixin,CreateView):
    model = Pet
    template_name = 'pet/pet_new.html'
    fields = ('pet_name', 'pet_type', 'pet_age','pet_breed')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ReportListView( ListView):
    model = Report
    template_name = 'pet/report_list.html'

class ReportCreateView(CreateView):
    model = Report
    template_name = 'pet/report_new.html'
    fields = ('reportName', 'reportType', 'reportDetails')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.pet = self.request.pet
        return super().form_valid(form)