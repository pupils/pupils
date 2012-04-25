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
#import ho.pisa as pisa
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string

from registration import signals
from forms import HijoExtraForm
from users.models import Padre, Hijo

from pupils.tablon.views import tipo_usuario
from pupils.encuesta.models import Encuesta

def generar_pdf(html):
	# Función para generar el archivo PDF y devolverlo mediante HttpResponse
	result = StringIO.StringIO()
	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), mimetype='application/pdf')
	return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def diploima_pdf(request):
	# vista de ejemplo con un hipotético modelo Libro
	# hijo=Hijo.objects.get(id=request.user.id)
	hijo=Hijo.objects.get(id = 1)
	html = render_to_string('diploma.html', {'pageorientation':'landscape','pagesize':'A4', 'hijo':hijo}, context_instance=RequestContext(request))
	return generar_pdf(html)

@login_required
def panel(request):
	
	entrando = tipo_usuario(request.user)
	if entrando == None:
		entrando = 'padre'
	context= { 
		'usuario': entrando,  
	}
	
	return render_to_response('users/panel.html',
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
			
			new_user.set_password(request.POST['password1'])
			new_user.username = request.POST['username']
			new_user.first_name = request.POST['name']
			new_user.last_name = request.POST['surname']
			new_user.email = request.POST['email']
			new_user.is_active = True
			new_user.save()
			
			hijo = Hijo(user=new_user)
			padre = Padre.objects.get(user=request.user)
			hijo.activity_id = padre.activity_id
			hijo.year = request.POST['year']
			hijo.observations = request.POST['observations']
			hijo.save()
			padre.children.add(hijo)
			padre.save()
			
			"""from registration.models import RegistrationManager, RegistrationProfile
			
			new_profile = RegistrationManager()
			new_profile.create_profile(new_user)
			new_profile.activation_key = RegistrationProfile.ACTIVATED
			
			"""
			signals.user_activated.send(sender='registration.backends.default.DefaultBackend',
                                        new_user= new_user,
                                        request = request)
			
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
	
	

def encuesta(request):
	
	lista = Encuesta.objects.all()
	context = {
		'lista_encuestas': lista
	}
	
	return render_to_response('encuesta/encuestas.html',
							context, 
							context_instance=RequestContext(request))
