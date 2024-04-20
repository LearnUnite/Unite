from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
import smtplib
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login ,logout
# Create your views here.



def index(request):
    if request.method == "POST":
      form = comment_form(request.POST)

      if form.is_valid():
        form = comment_form(request.POST)        
               
        name1 = form.data["first_name"]
        Email = form.data["email"]
        subj = form.data["subject"]
        msg = form.data["message"]
        send_mail(
           "COMMENT: {}".format(subj),
           "Username name: {}. MESSAGE:{}".format(name1, msg),
           "{}".format(Email),
           ["unitelearningpro17@gmail.com"],
           fail_silently=False,
            )
        return reverse_lazy('LEARN:index')      
    else:
        form = comment_form()
    
    return render(request, 'index.html', {'form':form})


@csrf_exempt 
def login_view(request): 
  if request.method == "POST":
    form = AuthenticationForm(data = request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)        
        return redirect('LEARN:index')
    else:        
        messages.warning(request,'invalid login!')
        return redirect('LEARN:login')
  else:
     form=AuthenticationForm() 
  
  form=AuthenticationForm()
  return render(request, 'login.html',{'form':form})       
             
  

@login_required
def logout_view(request):
    logout(request)
    return redirect('LEARN:index')

