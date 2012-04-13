# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms


@login_required
def panel(request):
	
	context= {
	    
	}
	
	return render_to_response('users/panel_control_padre.html',
							  context,
							  context_instance=RequestContext(request))
class UploadFileFrom (forms.Form):
	title = form.CharField(max_length=50)
	file = form.FileField()

def upload_pdf (request):
	
	if request.method == 'POST' :
		form = UploadFile(request.POST, request.FILES)
		if form.is_valid():
			archivo_por_subir(request.FILES['file']
			return HttpResponseRedirect('Subida hecha con exito')
		else:
			form = UploadFileFrom()
			return render_to_response('archivo.html',{'form': form})
