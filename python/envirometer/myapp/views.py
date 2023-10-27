from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    raw_body = request.body
    return HttpResponse(raw_body)
