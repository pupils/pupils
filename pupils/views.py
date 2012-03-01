from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return HttpResponse("Bienvenido a PUPILS CAMPUS APP")


def working(request):
    return render_to_response('working.html',context_instance=RequestContext(request))
