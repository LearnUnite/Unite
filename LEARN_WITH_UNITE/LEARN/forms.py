
from django import forms


class blog_login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class comment_form(forms.Form):
    first_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(max_length=250)
   