# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from tablon.forms import PostHijosForm
from users.models import Hijo, Padre
from tablon.models import Post

def tipo_usuario(user):
    try:
        hijo = user.hijo
        return "hijo"
    except Hijo.DoesNotExist:
        pass
    
    try:
        padre = user.padre
        return "padre"
    except Padre.DoesNotExist:
        pass
    
    return None
    

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

            form.save(hijos=hijos, publisher=request.user)
            
            msg = "Has añadido un nuevo trabajo. ¡Bien hecho!"
            correcto = True
            form = PostHijosForm()
                
        else:
            msg = "Algo ha fallado. ¡Ten cuidado!"
            correcto = False
            
        context = {
            "form" : form,
            "msg" : msg,
            "correcto" : correcto,
        }
        
        return render_to_response('tablon/form_hijo.html',
                                  context,
                                  context_instance=RequestContext(request))
        
    else:    
        form = PostHijosForm()
        context= {
            "form" : form,
        }
    
        return render_to_response('tablon/form_hijo.html',
                                  context,
                                  context_instance=RequestContext(request))
        
@login_required
def tablon(request):
    posts = []
    
    if tipo_usuario(request.user) == "hijo":
        posts = Post.objects.filter(hijo=request.user.hijo)
    elif tipo_usuario(request.user) == "padre":
        posts = Post.objects.filter(hijo__in=request.user.padre.children.all())
    
    
    context = {
        "posts" : posts,
    }
    
    return render_to_response('tablon/lista_posts.html',
                              context,
                              context_instance=RequestContext(request))
