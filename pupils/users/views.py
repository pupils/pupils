# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from pupils.users.forms import ProgenitorForm

def inscripcion(request, idactividad):
	
	if request.method == 'POST': 
		f = ProgenitorForm(request.POST) 
		if f.is_valid(): 
			# crear usuario
			# asociar usuario con actividad
			# ...
			print "Form OK"
			return render_to_response('users/inscripcion_ninio.html',
									  context_instance=RequestContext(request)
							         )
	else:
		f = ProgenitorForm()
        	
	context= {
	    'form': f,
	}
	return render_to_response('users/inscripcion_padre.html',
							  context,
							  context_instance=RequestContext(request)
							  )


def add_descendiente(request):
	return render_to_response('users/inscripcion_ninio.html',
							  context,
							  context_instance=RequestContext(request))
