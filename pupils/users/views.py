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
							  
def archivo_por_subir(archivo):
	destino = open('media/pagos/archivo.pdf','wb+')
	for chunk in archivo.chunks():
		destino.write(chunk)
	destino.close()

class UploadFileFrom(forms.Form):
	title = forms.CharField(max_length=50)
	file_id = forms.FileField()

def upload_pdf(request):
	
	if request.method == 'POST' :
		form = UploadFileFrom(request.POST, request.FILES)
		if forms.is_valid():
			archivo_por_subir(request.FILES['file_id'])
			return HttpResponseRedirect('/pcontrol/')
	else:
		forms = UploadFileFrom()
		return render_to_response('users/uploadpdf.html',{'form': forms}, context_instance=RequestContext(request))



