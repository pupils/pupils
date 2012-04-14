# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms

from registration.forms import RegistrationForm

class PadreExtraForm(RegistrationForm):
	phone_m = forms.CharField(max_length=10)
	phone_f = forms.CharField(max_length=10)

class HijoExtraForm(RegistrationForm):
	name = forms.CharField()
	surname = forms.CharField()
	year = forms.CharField(max_length=4)
	observations = forms.CharField()
