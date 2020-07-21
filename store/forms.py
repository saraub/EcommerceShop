from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
  

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude =['user']
        
        
class FilterForm(forms.Form):
    FILTER_CHOICES = (
        ('under 1 year of age', 'under 1 year of age'),
        ('timesince', 'Time Since'),
        ('timeuntil', 'Time Untill'),
    )

    filter_by = forms.ChoiceField(choices = FILTER_CHOICES)