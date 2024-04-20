from django import forms
from .models import *


class Biology_Form5_form(forms.ModelForm):
  class Meta:
             model = Biology_Form5
             fields = '__all__'

class Chemistry_Form5_form(forms.ModelForm):
  class Meta:
             model = Chemistry_Form5
             fields = '__all__'

class Economics_Form5_form(forms.ModelForm):
  class Meta:
             model = Economics_Form5
             fields = '__all__'

class General_Studies_Form5_form(forms.ModelForm):
  class Meta:
             model = General_Studies_Form5
             fields = '__all__'

class Geography_Form5_form(forms.ModelForm):
  class Meta:
             model = Geography_Form5
             fields = '__all__'

class History_Form5_form(forms.ModelForm):
  class Meta:
             model = History_Form5
             fields = '__all__'

class Kiswahili_Form5_form(forms.ModelForm):
  class Meta:
             model = Kiswahili_Form5
             fields = '__all__'

class Language_Form5_form(forms.ModelForm):
  class Meta:
             model = Language_Form5
             fields = '__all__'

class Mathematics_Form5_form(forms.ModelForm):
  class Meta:
             model = Mathematics_Form5
             fields = '__all__'

class Physics_Form5_form(forms.ModelForm):
  class Meta:
             model = Physics_Form5
             fields = '__all__'
