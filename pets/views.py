from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .forms import PetForm
from .models import models
from .models import Pet

class PetListView(ListView):
    model = Pet
    template_name = 'pet/pet_list.html'

class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet/pet_detail.html'
    login_url='login'

class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/pet_edit.html'

class PetCreateView(CreateView):
    model = Pet
    template_name = 'pet/pet_new.html'
    fields = ('pet_name','pet_type','pet_breed','pet_age')
    login_url='login'

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)