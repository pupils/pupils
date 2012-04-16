# -*- coding: utf-8 -*-

from django.contrib import admin
from pupils.encuesta.models import Encuesta, Pregunta, Respuesta

admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
