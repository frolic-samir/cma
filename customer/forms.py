from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerProfile

class CreateUserForm(UserCreationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-sm mb-2'}))
   first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
   last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
   password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm mb-2'}))
   password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm mb-2'}))

   class Meta:
      model    = User
      fields   = ['username','email','first_name', 'last_name','password1','password2']

class CustomerProfileForm(forms.ModelForm):
   name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-sm'}))
   contact = forms.CharField(max_length=14,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
   profile_pic = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))

   class Meta:
      model    = CustomerProfile
      exclude   = ['user']

class SignInForm(forms.Form):
   username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))

