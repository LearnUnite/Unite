from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone
from .forms import *
from django.views import generic
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView, FormView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login ,logout
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import *

#############################################################################################



###########################################################################

class Biology5ListView(ListView):
    model = Biology_Form5
    template_name = 'tutorials/biology/form5_list.html'

class Biology5DetailView(DetailView):
    model = Biology_Form5
    template_name = 'tutorials/biology/form5_detail.html'

class Biology5TopicCreateView(CreateView):
    model = Biology_Form5
    form_class = Biology5_Form
    template_name = 'forms/biology/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:bio5_list')

class Biology5VideoCreateView(CreateView):
    model = Biology5Tutorial
    form_class = Biology5_Tutorial_Form
    template_name = 'forms/biology/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:bio5_list')


def Biology5VideoDeleteView(request, pk):
   file = Biology5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:bio5_list')


def Biology5TopicDeleteView(request, pk):
   file = Biology_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:bio5_list')


###########################################################################

class Chemistry5ListView(ListView):
    model = Chemistry_Form5
    template_name = 'tutorials/chemistry/form5_list.html'

class Chemistry5DetailView(DetailView):
    model = Chemistry_Form5
    template_name = 'tutorials/chemistry/form5_detail.html'

class Chemistry5TopicCreateView(CreateView):
    model = Chemistry_Form5
    form_class = Chemistry5_Form
    template_name = 'forms/chemistry/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:chem5_list')

class Chemistry5VideoCreateView(CreateView):
    model = Chemistry5Tutorial
    form_class = Chemistry5_Tutorial_Form
    template_name = 'forms/chemistry/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:chem5_list')


def Chemistry5VideoDeleteView(request, pk):
   file = Chemistry5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:chem5_list')


def Chemistry5TopicDeleteView(request, pk):
   file = Chemistry_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:chem5_list')


###########################################################################

class Economics5ListView(ListView):
    model = Economics_Form5
    template_name = 'tutorials/economics/form5_list.html'

class Economics5DetailView(DetailView):
    model = Economics_Form5
    template_name = 'tutorials/economics/form5_detail.html'

class Economics5TopicCreateView(CreateView):
    model = Economics_Form5
    form_class = Economics5_Form
    template_name = 'forms/economics/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:eco5_list')

class Economics5VideoCreateView(CreateView):
    model = Economics5Tutorial
    form_class = Economics5_Tutorial_Form
    template_name = 'forms/economics/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:eco5_list')

def Economics5VideoDeleteView(request, pk):
   file = Economics5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:eco5_list')


def Economics5TopicDeleteView(request, pk):
   file = Economics_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:eco5_list')


###########################################################################

class English5ListView(ListView):
    model = English_Form5
    template_name = 'tutorials/english/form5_list.html'

class English5DetailView(DetailView):
    model = English_Form5
    template_name = 'tutorials/english/form5_detail.html'

class English5TopicCreateView(CreateView):
    model = English_Form5
    form_class = English5_Form
    template_name = 'forms/english/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:lang5_list')

class English5VideoCreateView(CreateView):
    model = English5Tutorial
    form_class = English5_Tutorial_Form
    template_name = 'forms/english/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:lang5_list')

def English5VideoDeleteView(request, pk):
   file = English5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:lang5_list')


def English5TopicDeleteView(request, pk):
   file = English_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:lang5_list')


###########################################################################

class Geography5ListView(ListView):
    model = Geography_Form5
    template_name = 'tutorials/geography/form5_list.html'

class Geography5DetailView(DetailView):
    model = Geography_Form5
    template_name = 'tutorials/geography/form5_detail.html'

class Geography5TopicCreateView(CreateView):
    model = Geography_Form5
    form_class = Geography5_Form
    template_name = 'forms/geography/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:geo5_list')

class Geography5VideoCreateView(CreateView):
    model = Geography5Tutorial
    form_class = Geography5_Tutorial_Form
    template_name = 'forms/geography/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:geo5_list')


def Geography5VideoDeleteView(request, pk):
   file = Geography5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:geo5_list')


def Geography5TopicDeleteView(request, pk):
   file = Geography_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:geo5_list')


###########################################################################

class History5ListView(ListView):
    model = History_Form5
    template_name = 'tutorials/history/form5_list.html'

class History5DetailView(DetailView):
    model = History_Form5
    template_name = 'tutorials/history/form5_detail.html'

class History5TopicCreateView(CreateView):
    model = History_Form5
    form_class = History5_Form
    template_name = 'forms/history/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:his5_list')

class History5VideoCreateView(CreateView):
    model = History5Tutorial
    form_class = History5_Tutorial_Form
    template_name = 'forms/history/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:his5_list')


def History5VideoDeleteView(request, pk):
   file = History5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:his5_list')


def History5TopicDeleteView(request, pk):
   file = History_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:his5_list')


###########################################################################

class Kiswahili5ListView(ListView):
    model = Kiswahili_Form5
    template_name = 'tutorials/kiswahili/form5_list.html'

class Kiswahili5DetailView(DetailView):
    model = Kiswahili_Form5
    template_name = 'tutorials/kiswahili/form5_detail.html'

class Kiswahili5TopicCreateView(CreateView):
    model = Kiswahili_Form5
    form_class = Kiswahili5_Form
    template_name = 'forms/kiswahili/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:kis5_list')

class Kiswahili5VideoCreateView(CreateView):
    model = Kiswahili5Tutorial
    form_class = Kiswahili5_Tutorial_Form
    template_name = 'forms/kiswahili/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:kis5_list')



def Kiswahili5VideoDeleteView(request, pk):
   file = Kiswahili5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:kis5_list')


def Kiswahili5TopicDeleteView(request, pk):
   file = Kiswahili_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:kis5_list')


##########################################################################

class Mathematics5ListView(ListView):
    model = Mathematics_Form5
    template_name = 'tutorials/mathematics/form5_list.html'

class Mathematics5DetailView(DetailView):
    model = Mathematics_Form5
    template_name = 'tutorials/mathematics/form5_detail.html'

class Mathematics5TopicCreateView(CreateView):
    model = Mathematics_Form5
    form_class = Mathematics5_Form
    template_name = 'forms/mathematics/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:math5_list')

class Mathematics5VideoCreateView(CreateView):
    model = Mathematics5Tutorial
    form_class = Mathematics5_Tutorial_Form
    template_name = 'forms/mathematics/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:math5_list')


def Mathematics5VideoDeleteView(request, pk):
   file = Mathematics5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:math5_list')


def Mathematics5TopicDeleteView(request, pk):
   file = Mathematics_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:math5_list')


##########################################################################


class Physics5ListView(ListView):
    model = Physics_Form5
    template_name = 'tutorials/physics/form5_list.html'

class Physics5DetailView(DetailView):
    model = Physics_Form5
    template_name = 'tutorials/physics/form5_detail.html'

class Physics5TopicCreateView(CreateView):
    model = Physics_Form5
    form_class = Physics5_Form
    template_name = 'forms/physics/tutorials/form5_topic.html'
    success_url = reverse_lazy('TUTORIALS:phy5_list')

class Physics5VideoCreateView(CreateView):
    model = Physics5Tutorial
    form_class = Physics5_Tutorial_Form
    template_name = 'forms/physics/tutorials/form5.html'
    success_url = reverse_lazy('TUTORIALS:phy5_list')


def Physics5VideoDeleteView(request, pk):
   file = Physics5Tutorial.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:phy5_list')


def Physics5TopicDeleteView(request, pk):
   file = Physics_Form5.objects.filter(pk=pk)
   file.delete()
   return redirect('TUTORIALS:phy5_list')
