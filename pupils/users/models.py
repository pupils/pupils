# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from pupils.actividad.models import Actividad

"""
        Campos del modelo usuario de django - clase User
        username
	    first_name
		last_name
		email
		password
		is_staff
		is_active
		is_superuser
		last_login
		date_joined
"""
     
class Hijo(models.Model):
    user = models.OneToOneField(User)
    activity_id = models.IntegerField(null=False)
    year = models.CharField(max_length='4')
    observations = models.TextField()
    
class Padre(models.Model):
    user = models.OneToOneField(User)
    activity_id = models.IntegerField(null=False)
    children = models.ManyToManyField(Hijo)
    phone_f = models.CharField(max_length='10')
    phone_m = models.CharField(max_length='10')
