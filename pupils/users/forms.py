# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from users.models import Progenitor

class ProgenitorForm(ModelForm):
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
	pass
	#user = forms.CharField(max_length=100)
	#fecha_nacimiento = forms.DateTimeField()
	#direccion = forms.CharField(max_length=100)
	#progenitor = forms.ForeignKey(Progenitor)
	#fecha_nacimiento = forms.DateTimeField()
	#necesidades = forms.TextField()
