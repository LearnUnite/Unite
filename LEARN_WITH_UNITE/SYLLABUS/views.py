from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from SYLLABUS.models import *
from SYLLABUS.forms import *
# Create your views here.

class biology_form5(ListView):
    model = Biology_Form5
    template_name = 'syllabus/biology/form5.html'


class CreateBiology_Form5File(CreateView):
    model = Biology_Form5
    form_class = Biology_Form5_form
    template_name = 'forms/biology/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:bio_form5')



def DeleteBiology_Form5File(request, pk):
   file = Biology_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:bio_form5')


###################################################################################################################

class chemistry_form5(ListView):
    model = Chemistry_Form5
    template_name = 'syllabus/chemistry/form5.html'


class CreateChemistry_Form5File(CreateView):
    model = Chemistry_Form5
    form_class = Chemistry_Form5_form
    template_name = 'forms/chemistry/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:chem_form5')


def DeleteChemistry_Form5File(request, pk):
   file = Chemistry_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:chem_form5')


###################################################################################################################


class economics_form5(ListView):
    model = Economics_Form5
    template_name = 'syllabus/economics/form5.html'


class CreateEconomics_Form5File(CreateView):
    model = Economics_Form5
    form_class = Economics_Form5_form
    template_name = 'forms/economics/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:eco_form5')


def DeleteEconomics_Form5File(request, pk):
   file = Economics_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:eco_form5')


###################################################################################################################


class general_studies_form5(ListView):
    model = General_Studies_Form5
    template_name = 'syllabus/general_studies/form5.html'


class CreateGeneral_Studies_Form5File(CreateView):
    model = General_Studies_Form5
    form_class = General_Studies_Form5_form
    template_name = 'forms/general_studies/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:gs_form5')


def DeleteGeneral_Studies_Form5File(request, pk):
   file = General_Studies_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:gs_form5')


###################################################################################################################


class geography_form5(ListView):
    model = Geography_Form5
    template_name = 'syllabus/geography/form5.html'


class CreateGeography_Form5File(CreateView):
    model = Geography_Form5
    form_class = Geography_Form5_form
    template_name = 'forms/geography/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:geo_form5')


def DeleteGeography_Form5File(request, pk):
   file = Geography_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:geo_form5')



###################################################################################################################


class history_form5(ListView):
    model = History_Form5
    template_name = 'syllabus/history/form5.html'


class CreateHistory_Form5File(CreateView):
    model = History_Form5
    form_class = History_Form5_form
    template_name = 'forms/history/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:his_form5')

def DeleteHistory_Form5File(request, pk):
   file = History_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:his_form5')


###################################################################################################################


class kiswahili_form5(ListView):
    model = Kiswahili_Form5
    template_name = 'syllabus/kiswahili/form5.html'


class CreateKiswahili_Form5File(CreateView):
    model = Kiswahili_Form5
    form_class = Kiswahili_Form5_form
    template_name = 'forms/kiswahili/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:kis_form5')


def DeleteKiswahili_Form5File(request, pk):
   file = Kiswahili_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:kis_form5')


###################################################################################################################


class language_form5(ListView):
    model = Language_Form5
    template_name = 'syllabus/english/form5.html'


class CreateLanguage_Form5File(CreateView):
    model = Language_Form5
    form_class = Language_Form5_form
    template_name = 'forms/english/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:lang_form5')


def DeleteLanguage_Form5File(request, pk):
   file = Language_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:lang_form5')


###################################################################################################################


class mathematics_form5(ListView):
    model = Mathematics_Form5
    template_name = 'syllabus/mathematics/form5.html'


class CreateMathematics_Form5File(CreateView):
    model = Mathematics_Form5
    form_class = Mathematics_Form5_form
    template_name = 'forms/mathematics/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:math_form5')


def DeleteMathematics_Form5File(request, pk):
   file = Mathematics_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:math_form5')


###################################################################################################################


class physics_form5(ListView):
    model = Physics_Form5
    template_name = 'syllabus/physics/form5.html'


class CreatePhysics_Form5File(CreateView):
    model = Physics_Form5
    form_class = Physics_Form5_form
    template_name = 'forms/physics/syllabus/form5.html'
    success_url = reverse_lazy('SYLLABUS:phy_form5')

def DeletePhysics_Form5File(request, pk):
   file = Physics_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('SYLLABUS:phy_form5')



    