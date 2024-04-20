from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView ,DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.

class biology_form5(ListView):
    model = Biology_Form5
    template_name = 'notes/biology/form5.html'


class CreateBiology_Form5Notes(CreateView):
    model = Biology_Form5
    form_class = Biology_Form5_form
    template_name = 'forms/biology/notes/form5.html'
    success_url = reverse_lazy('NOTES:bio_form5')


def DeleteBiology_Form5Notes(request, pk):
   notes = Biology_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:bio_form5')


########################################################################################

class chemistry_form5(ListView):
    model = Chemistry_Form5
    template_name = 'notes/chemistry/form5.html'


class CreateChemistry_Form5Notes(CreateView):
    model = Chemistry_Form5
    form_class = Chemistry_Form5_form
    template_name = 'forms/chemistry/notes/form5.html'
    success_url = reverse_lazy('NOTES:chem_form5')


def DeleteChemistry_Form5Notes(request, pk):
   notes = Chemistry_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:chem_form5')


########################################################################################


class economics_form5(ListView):
    model = Economics_Form5
    template_name = 'notes/economics/form5.html'


class CreateEconomics_Form5Notes(CreateView):
    model = Economics_Form5
    form_class = Economics_Form5_form
    template_name = 'forms/economics/notes/form5.html'
    success_url = reverse_lazy('NOTES:eco_form5')


def DeleteEconomics_Form5Notes(request, pk):
   notes = Economics_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:eco_form5')



########################################################################################


class general_studies_form5(ListView):
    model = General_Studies_Form5
    template_name = 'notes/general_studies/form5.html'


class CreateGeneral_Studies_Form5Notes(CreateView):
    model = General_Studies_Form5
    form_class = General_Studies_Form5_form
    template_name = 'forms/general_studies/notes/form5.html'
    success_url = reverse_lazy('NOTES:gs_form5')


def DeleteGeneral_Studies_Form5Notes(request, pk):
   notes = General_Studies_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:gs_form5')


########################################################################################


class geography_form5(ListView):
    model = Geography_Form5
    template_name = 'notes/geography/form5.html'


class CreateGeography_Form5Notes(CreateView):
    model = Geography_Form5
    form_class = Geography_Form5_form
    template_name = 'forms/geography/notes/form5.html'
    success_url = reverse_lazy('NOTES:geo_form5')


def DeleteGeography_Form5Notes(request, pk):
   notes = Geography_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:geo_form5')


########################################################################################


class history_form5(ListView):
    model = History_Form5
    template_name = 'notes/history/form5.html'


class CreateHistory_Form5Notes(CreateView):
    model = History_Form5
    form_class = History_Form5_form
    template_name = 'forms/history/notes/form5.html'
    success_url = reverse_lazy('NOTES:his_form5')


def DeleteHistory_Form5Notes(request, pk):
   notes = History_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:his_form5')


########################################################################################


class kiswahili_form5(ListView):
    model = Kiswahili_Form5
    template_name = 'notes/kiswahili/form5.html'


class CreateKiswahili_Form5Notes(CreateView):
    model = Kiswahili_Form5
    form_class = Kiswahili_Form5_form
    template_name = 'forms/kiswahili/notes/form5.html'
    success_url = reverse_lazy('NOTES:kis_form5')


def DeleteKiswahili_Form5Notes(request, pk):
   notes = Kiswahili_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:kis_form5')


########################################################################################

class language_form5(ListView):
    model = Language_Form5
    template_name = 'notes/english/form5.html'


class CreateLanguage_Form5Notes(CreateView):
    model = Language_Form5
    form_class = Language_Form5_form
    template_name = 'forms/english/notes/form5.html'
    success_url = reverse_lazy('NOTES:lang_form5')


def DeleteLanguage_Form5Notes(request, pk):
   notes = Language_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:lang_form5')


########################################################################################

class mathematics_form5(ListView):
    model = Mathematics_Form5
    template_name = 'notes/mathematics/form5.html'


class CreateMathematics_Form5Notes(CreateView):
    model = Mathematics_Form5
    form_class = Mathematics_Form5_form
    template_name = 'forms/mathematics/notes/form5.html'
    success_url = reverse_lazy('NOTES:math_form5')


def DeleteMathematics_Form5Notes(request, pk):
   notes = Mathematics_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:math_form5')


########################################################################################


class physics_form5(ListView):
    model = Physics_Form5
    template_name = 'notes/physics/form5.html'


class CreatePhysics_Form5Notes(CreateView):
    model = Physics_Form5
    form_class = Physics_Form5_form
    template_name = 'forms/physics/notes/form5.html'
    success_url = reverse_lazy('NOTES:phy_form5')


def DeletePhysics_Form5Notes(request, pk):
   notes = Physics_Form5.objects.filter(pk=pk)
   notes.delete()
   return redirect('NOTES:phy_form5')



########################################################################################


    