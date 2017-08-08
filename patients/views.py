from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from patients.models import Bloodgroup, Patient

# Create your views here.
class BloodgroupList(ListView):
    model = Bloodgroup
    template_name = 'patients/bloodgroup_list.html'
    #context_object_name = 'bloodgroup_list'
    
class BloodgroupCreate(CreateView):
    model = Bloodgroup
    #fields =  []
    fields =  "__all__"

    #def form_valid(self, form):
    #        form.instance.createby = self.request.user.username
    #        return super(PortfolioCreate, self).form_valid(form)

# Create your views here.
class PatientList(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    #context_object_name = 'patient_list'
    #paginate_by = 20
