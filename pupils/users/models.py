# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Direccion(models.Model):
	calle = models.CharField(max_length='100')
	numero = models.CharField(max_length='5')
	codigo_postal = models.CharField(max_length='6')
	localidad = models.CharField(max_length='50')
	provincia = models.CharField(max_length='35')
	pais = models.CharField(max_length='35')

class Progenitor(models.Model):
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
    user = models.ForeignKey(User, unique=True)
    direccion = models.ForeignKey(Direccion, unique=True)
    profesion = models.CharField(max_length='100')
    observaciones = models.TextField()

class Descendiente(models.Model):
	user = models.ForeignKey(User, unique=True)
	progenitor = models.ForeignKey(Progenitor)
	fecha_nacimiento = models.DateTimeField()
	necesidades = models.TextField()
