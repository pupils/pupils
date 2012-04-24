from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pupils.actividad.models import Actividad

def encuesta_rellenar(request,idencuesta):
	try:
		enc = Encuesta.objects.get(id=idencuesta)[0]
		preguntas = Pregunta.objects.get(encuesta = enc)
	except:
		preguntas = False
	
	context = { 'titulo': enc.titulo,
			'preguntas' : preguntas,}
	
	return render_to_response('encuesta/encuesta_detalle.html',context,context_instance=RequestContext(request))
