# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from users.models import Progenitor
from registration.forms import RegistrationForm

class PadreExtraForm(RegistrationForm):
	phone_m = forms.CharField(max_length=10)
	phone_f = forms.CharField(max_length=10)

class ProgenitorForm(ModelForm):
	name = forms.CharField(max_length=100)
	surname = forms.CharField(max_length=100)
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirm = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(max_length=100)
	phone_a = forms.CharField(max_length=10)
	phone_b = forms.CharField(max_length=10)

	class Meta:
		model = Progenitor
		exclude = ["user","direccion","profesion", "observaciones"]

class DescendienteForm(forms.Form):
	name = forms.CharField(max_length=100)
	surname = forms.CharField(max_length=100)
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirm = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(max_length=100)
	birth_date = forms.DateField()
	observation = forms.CharField(200)
