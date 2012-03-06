# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from users.models import Progenitor

class ProgenitorForm(ModelForm):
	username = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirm = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = Progenitor
		exclude = ["user"]
		
	#user = forms.CharField(max_length=100)
	#fecha_nacimiento = forms.DateTimeField()
	#profesion = forms.CharField(max_length=30)
	#direccion = forms.CharField(max_length=100)
	#observaciones = forms.TextField()

class DescendienteForm(forms.Form):
	pass
	#user = forms.CharField(max_length=100)
	#fecha_nacimiento = forms.DateTimeField()
	#direccion = forms.CharField(max_length=100)
	#progenitor = forms.ForeignKey(Progenitor)
	#fecha_nacimiento = forms.DateTimeField()
	#necesidades = forms.TextField()
