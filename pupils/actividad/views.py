from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pupils.actividad.models import Actividad

def detalle(request,idactividad):
	
	try:
	    act = Actividad.objects.get(id=idactividad)
	except:
		act = False
	
	context = {'actividad' : act,}
	
	return render_to_response('actividad/actividad_detalle.html',context,context_instance=RequestContext(request))
