# -*- coding: utf-8 -*-
from django.db import models
import datetime
## titulo, lugar, fecha, observaciones, pùblico, rango de edades, 
##
##

# Create your models here.

class Actividad(models.Model):
	"""
		Campos del modelo actividad de django - clase Actividad
	"""
	#GENDER_CHOICES_EQUIPMENT = (
	#	('L', 'Linterna'),
	#	('C', 'Cantimplora'),
	#)
	title = models.TextField() # Titulo
	descripcion = models.TextField() # Descripcion de la actividad
	place = models.TextField() # Lugar
	date_start = models.DateTimeField() #Fecha inicio y fin
	date_end = models.DateTimeField()
	timetable = models.TextField() # Horarios y otras explicaciones (p.e. la actividad es solo martes y jueves de 8 a 15 horas.)
	age_range = models.CharField(max_length='100') # Rango de edades
	equipment = models.TextField() # Equipamiento para la actividad	
	notes = models.TextField() # Observaciones
