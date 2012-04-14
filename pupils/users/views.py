# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

from forms import HijoExtraForm
from users.models import Padre

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
		forms = UploadFileFrom(request.POST, request.FILES)
		if forms.is_valid():
			archivo_por_subir(request.FILES['file_id'])
			return HttpResponseRedirect('/pcontrol/')
		else:
			
			return HttpResponse("Payoooooo")
						
	else:
		forms = UploadFileFrom()
	return render_to_response('users/uploadpdf.html',{'form': forms}, context_instance=RequestContext(request))

def inscribir_hijo(request):
	
	if request.method == 'POST' :
		forms = HijoExtraForm(request.POST, request.FILES)
		
		if forms.is_valid():
			padre = Padre.objects.get(id=request.user.id)
			print padre.user.username
			
			"""new_user = User()
			new_user.password = request.POST['password']
			new_user.username = request.POST['username']
			new_user.activate = True
			custom = Hijo(user=new_user)
			custom.activity_id = 1
			custom.year = request.POST['year']
			custom.observations = request.POST['observations']
			custom.save()
			#asociar hijo a padre
			#archivo_por_subir(request.FILES['file_id'])"""
			return HttpResponseRedirect('/pcontrol/')
		else:
			context= {
				'form': forms,
				'hijo': True,
			}
			return render_to_response('registration/registration_form.html',
									context, 
									context_instance=RequestContext(request))
						
	else:
		forms = HijoExtraForm()
	
	context= {
		'form': forms,
	    'hijo': True,
	}
	
	return render_to_response('registration/registration_form.html',
							context, 
							context_instance=RequestContext(request))
	
	

