# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

from registration import signals
from forms import HijoExtraForm
from users.models import Padre, Hijo

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
			return render_to_response('users/uploadpdf.html',{'form': forms}, context_instance=RequestContext(request))
						
	else:
		forms = UploadFileFrom()
	return render_to_response('users/uploadpdf.html',{'form': forms}, context_instance=RequestContext(request))

def inscribir_hijo(request):
	
	if request.method == 'POST' :
		forms = HijoExtraForm(request.POST, request.FILES)
		
		if forms.is_valid():
			new_user = User()
			new_user.password = request.POST['password1']
			new_user.username = request.POST['username']
			new_user.first_name = request.POST['name']
			new_user.last_name = request.POST['surname']
			new_user.email = request.POST['email']
			new_user.activate = True
			new_user.save()
			
			hijo = Hijo(user=new_user)
			padre = Padre.objects.get(user=request.user)
			hijo.activity_id = padre.activity_id
			hijo.year = request.POST['year']
			hijo.observations = request.POST['observations']
			hijo.save()
			padre.children.add(hijo)
			padre.save()
			
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
	
	

