# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User

from actividad.models import Actividad

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

class Post(models.Model):
    title = models.TextField(null=True, blank=True) #Título
    content = models.TextField() #Contenido de la entrada
    
    actividad = models.ForeignKey(Actividad) #Actividad con la que está relacionada
    # grupo = models.ManyToManyField(Grupo, null=True, blank=True)
    #descendientes = models.ManyToManyField(Descendiente, null=True, blank=True)
    
    date_creation = models.DateTimeField(auto_now_add=True)
    published_by = models.ForeignKey(User)
    
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    
