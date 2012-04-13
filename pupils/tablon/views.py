# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from tablon.forms import PostHijosForm

@login_required
def nuevo_post_hijo(request):

    form = PostHijosForm()
    context= {}

    return render_to_response('tablon/form_hijo.html',
                              context,
                              context_instance=RequestContext(request))
