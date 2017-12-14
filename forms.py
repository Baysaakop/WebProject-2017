from django import forms
from .models import Student
from django.forms import  ChoiceField
from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div

class NewStudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['firstname','lastname','age','phone_number','major']
