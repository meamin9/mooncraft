# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("You're at the mc01 index.")

def enter(request):
    url = GameUrl.objects.all()[0].res_url
    return HttpResponse(url)

def res(request, uri):
    return HttpResponse("res")
