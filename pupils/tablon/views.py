# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from tablon.forms import PostHijosForm
from users.models import Hijo

@login_required
def nuevo_post_hijo(request):

    if request.method == "POST":
        
        form = PostHijosForm(request.POST)
        if form.is_valid():
            try:
                hijos = []
                hijos.append(request.user.hijo)
            except Hijo.DoesNotExist:
                print "*"*20
                print "No es un hijo"
                print "*"*20
            #print form.save()
            print form.save(hijos=hijos, publisher=request.user)
            return HttpResponse("Hecho correctamente.")
                
        else:
            return HttpResponse("No realizado.")
    
    else:    
        form = PostHijosForm()
        context= {
            "form" : form,
        }
    
        return render_to_response('tablon/form_hijo.html',
                                  context,
                                  context_instance=RequestContext(request))
    
    
    
