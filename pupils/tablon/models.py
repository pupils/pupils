# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from users.models import Hijo 

class Post(models.Model):
    title = models.TextField(null=True, blank=True) #Título
    content = models.TextField(null=True, blank=True) #Contenido de la entrada
    url = models.URLField(max_length=200, null=True, blank=True)
    
    hijo = models.ForeignKey(Hijo)
    
    date_creation = models.DateTimeField(auto_now_add=True)
    published_by = models.ForeignKey(User)
    

    
