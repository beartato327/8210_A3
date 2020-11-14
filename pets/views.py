from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .forms import PetForm 
from .models import Pet, Report

class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    template_name = 'pet/pet_list.html'

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

class PetDetailView(LoginRequiredMixin,DetailView):
    model = Pet
    template_name = 'pet/pet_detail.html'
    login_url='login'
    queryset = Pet.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PetDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.all()
        return context

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
        form.instance.pet_id = self.kwargs.get('pk')
        return super(ReportCreateView, self).form_valid(form)

class ReportDetailView(LoginRequiredMixin,DetailView):
    model = Report
    template_name = 'pet/report_detail.html'
    login_url='login'