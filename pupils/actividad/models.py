# -*- coding: utf-8 -*-
from django.db import models
import datetime

class Actividad(models.Model):

	title = models.TextField() 
	descripcion = models.TextField() 
	place = models.TextField() 
	date_start = models.DateTimeField() 
	date_end = models.DateTimeField()
	timetable = models.TextField() 
	age_range = models.CharField(max_length='100') 
	equipment = models.TextField() 
	notes = models.TextField()
