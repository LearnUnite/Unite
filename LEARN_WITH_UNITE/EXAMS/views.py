from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from EXAMS.models import *
from .forms import *
# Create your views here.

class biology_form5(ListView):
    model = Biology_Form5
    template_name = 'exams/biology/form5.html'


class CreateBiology_Form5Exams(CreateView):
    model = Biology_Form5
    form_class = Biology_Form5_form
    template_name = 'forms/biology/exams/form5.html'
    success_url = reverse_lazy('EXAMS:bio_form5')


def DeleteBiology_Form5Exams(request, pk):
   exam = Biology_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:bio_form5')


#####################################################################################################################

class chemistry_form5(ListView):
    model = Chemistry_Form5
    template_name = 'exams/chemistry/form5.html'


class CreateChemistry_Form5Exams(CreateView):
    model = Chemistry_Form5
    form_class = Chemistry_Form5_form
    template_name = 'forms/chemistry/exams/form5.html'
    success_url = reverse_lazy('EXAMS:chem_form5')


def DeleteChemistry_Form5Exams(request, pk):
   exam = Chemistry_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:chem_form5')


#####################################################################################################################


class economics_form5(ListView):
    model = Economics_Form5
    template_name = 'exams/economics/form5.html'


class CreateEconomics_Form5Exams(CreateView):
    model = Economics_Form5
    form_class = Economics_Form5_form
    template_name = 'forms/economics/exams/form5.html'
    success_url = reverse_lazy('EXAMS:eco_form5')

def DeleteEconomics_Form5Exams(request, pk):
   exam = Economics_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:eco_form5')


#####################################################################################################################



class general_studies_form5(ListView):
    model = General_Studies_Form5
    template_name = 'exams/general_studies/form5.html'


class CreateGeneral_Studies_Form5Exams(CreateView):
    model = General_Studies_Form5
    form_class = General_Studies_Form5_form
    template_name = 'forms/general_studies/exams/form5.html'
    success_url = reverse_lazy('EXAMS:gs_form5')


def DeleteGeneral_Studies_Form5Exams(request, pk):
   exam = General_Studies_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:gs_form5')


#####################################################################################################################


class geography_form5(ListView):
    model = Geography_Form5
    template_name = 'exams/geography/form5.html'


class CreateGeography_Form5Exams(CreateView):
    model = Geography_Form5
    form_class = Geography_Form5_form
    template_name = 'forms/geography/exams/form5.html'
    success_url = reverse_lazy('EXAMS:geo_form5')


def DeleteGeography_Form5Exams(request, pk):
   exam = Geography_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:geo_form5')


#####################################################################################################################


class history_form5(ListView):
    model = History_Form5
    template_name = 'exams/history/form5.html'


class CreateHistory_Form5Exams(CreateView):
    model = History_Form5
    form_class = History_Form5_form
    template_name = 'forms/history/exams/form5.html'
    success_url = reverse_lazy('EXAMS:his_form5')


def DeleteHistory_Form5Exams(request, pk):
   exam = History_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:his_form5')


#####################################################################################################################


class kiswahili_form5(ListView):
    model = Kiswahili_Form5
    template_name = 'exams/kiswahili/form5.html'


class CreateKiswahili_Form5Exams(CreateView):
    model = Kiswahili_Form5
    form_class = Kiswahili_Form5_form
    template_name = 'forms/kiswahili/exams/form5.html'
    success_url = reverse_lazy('EXAMS:kis_form5')


def DeleteKiswahili_Form5Exams(request, pk):
   exam = Kiswahili_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:kis_form5')


#####################################################################################################################


class language_form5(ListView):
    model = Language_Form5
    template_name = 'exams/english/form5.html'


class CreateLanguage_Form5Exams(CreateView):
    model = Language_Form5
    form_class = Language_Form5_form
    template_name = 'forms/english/exams/form5.html'
    success_url = reverse_lazy('EXAMS:lang_form5')


def DeleteLanguage_Form5Exams(request, pk):
   exam = Language_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:lang_form5')


#####################################################################################################################


class mathematics_form5(ListView):
    model = Mathematics_Form5
    template_name = 'exams/mathematics/form5.html'


class CreateMathematics_Form5Exams(CreateView):
    model = Mathematics_Form5
    form_class = Mathematics_Form5_form
    template_name = 'forms/mathematics/exams/form5.html'
    success_url = reverse_lazy('EXAMS:math_form5')

def DeleteMathematics_Form5Exams(request, pk):
   exam = Mathematics_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:math_form5')


#####################################################################################################################


class physics_form5(ListView):
    model = Physics_Form5
    template_name = 'exams/physics/form5.html'


class CreatePhysics_Form5Exams(CreateView):
    model = Physics_Form5
    form_class = Physics_Form5_form
    template_name = 'forms/physics/exams/form5.html'
    success_url = reverse_lazy('EXAMS:phy_form5')


def DeletePhysics_Form5Exams(request, pk):
   exam = Physics_Form5.objects.filter(pk=pk)
   exam.delete()
   return redirect('EXAMS:phy_form5')


#####################################################################################################################


    