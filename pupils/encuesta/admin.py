# -*- coding: utf-8 -*-

from django.contrib import admin
from pupils.encuesta.models import Encuesta, Pregunta

admin.site.register(Pregunta)
admin.site.register(Encuesta)

