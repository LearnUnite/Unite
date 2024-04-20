from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.core import validators
from .models import *

##################################################################


#########################################################################

class Biology5_Form(forms.ModelForm):
    class Meta:
        model = Biology_Form5
        fields = '__all__'

class Biology5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = Biology5Tutorial
        fields = '__all__'


#########################################################################

class Chemistry5_Form(forms.ModelForm):
    class Meta:
        model = Chemistry_Form5
        fields = '__all__'

class Chemistry5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = Chemistry5Tutorial
        fields = '__all__'


#########################################################################

class Economics5_Form(forms.ModelForm):
    class Meta:
        model = Economics_Form5
        fields = '__all__'

class Economics5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = Economics5Tutorial
        fields = '__all__'

#########################################################################

class English5_Form(forms.ModelForm):
    class Meta:
        model = English_Form5
        fields = '__all__'

class English5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = English5Tutorial
        fields = '__all__'

########################################################################

class Geography5_Form(forms.ModelForm):
    class Meta:
        model = Geography_Form5
        fields = '__all__'

class Geography5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = Geography5Tutorial
        fields = '__all__'

########################################################################

class History5_Form(forms.ModelForm):
    class Meta:
        model = History_Form5
        fields = '__all__'

class History5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = History5Tutorial
        fields = '__all__'

########################################################################

class Kiswahili5_Form(forms.ModelForm):
    class Meta:
        model = Kiswahili_Form5
        fields = '__all__'

class Kiswahili5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = Kiswahili5Tutorial
        fields = '__all__'

########################################################################

class Mathematics5_Form(forms.ModelForm):
    class Meta:
        model = Mathematics_Form5
        fields = '__all__'

class Mathematics5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = Mathematics5Tutorial
        fields = '__all__'

###########################################################################

class Physics5_Form(forms.ModelForm):
    class Meta:
        model = Physics_Form5
        fields = '__all__'

class Physics5_Tutorial_Form(forms.ModelForm):
    class Meta:
        model = Physics5Tutorial
        fields = '__all__'

#########################################################################
