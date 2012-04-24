from django.db import models


class Respuesta(models.Model):
	respuesta = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.respuesta

class Pregunta(models.Model):
	pregunta = models.CharField(max_length=200)
	respuesta = models.OneToOneField(Respuesta)
	
	def __unicode__(self):
		return self.pregunta

class Encuesta(models.Model):
    titulo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    preguntas = models.ManyToManyField(Pregunta)
        
    def __unicode__(self):
        return self.titulo
