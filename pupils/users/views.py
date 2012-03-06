# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from pupils.users.forms import ProgenitorForm

def inscripcion(request, idactividad):
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
