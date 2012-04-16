from django.db import models

class Encuesta(models.Model):
    titulo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
        
    def __unicode__(self):
        return self.titulo

class Pregunta(models.Model):
	encuesta = models.ForeignKey(Encuesta)
	pregunta = models.CharField(max_length=200)

	def __unicode__(self):
		return self.pregunta
            
class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    respuesta = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.respuesta
