# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from pupils.users.forms import ProgenitorForm, DescendienteForm




def panel(request):
	
	context= {
	    
	}
	
	return render_to_response('users/panel_control_padre.html',
							  context,
							  context_instance=RequestContext(request))



def progenitor(request, idactividad):
	
	if request.method == 'POST': 
		f = ProgenitorForm(request.POST) 
		if f.is_valid(): 
			# crear usuario
			# asociar usuario con actividad
			# ...
			print "Form OK"
			url = "/actividad/nuevo/participante/%s/" % idactividad
			return HttpResponseRedirect(url)
	else:
		f = ProgenitorForm()
        	
	context= {
	    'form': f,
	}
	return render_to_response('users/inscripcion_padre.html',
							  context,
							  context_instance=RequestContext(request)
							  )


def participante(request, idactividad):
	
	if request.method == 'POST': 
		f = DescendienteForm(request.POST) 
		if f.is_valid(): 
			# crear usuario
			# asociar usuario con progenitor
			# ...
			print "Form OK"
			return render_to_response('users/inscripcion_done.html',
									  context_instance=RequestContext(request)
							         )
	else:
		f = DescendienteForm()
        	
	context= {
	    'form': f,
	}
	
	return render_to_response('users/inscripcion_ninio.html',
							  context,
							  context_instance=RequestContext(request))
