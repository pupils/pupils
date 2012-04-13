# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from tablon.forms import PostHijosForm

@login_required
def nuevo_post_hijo(request):

    if request.method == "POST":
        form = PostHijosForm(request)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = PostHijosForm()
        context= {
            "form" : form,
        }
    
        return render_to_response('tablon/form_hijo.html',
                                  context,
                                  context_instance=RequestContext(request))
    
    
    
