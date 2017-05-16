# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import GameUrl
from django.http import StreamingHttpResponse
from mooncraft.settings import STATIC_ROOT as static_root

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("You're at the mc01 index.")

def enter(request):
    url = GameUrl.objects.all()[0].res_url
    return HttpResponse(url)

def res(request, uri, version=None):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    file_name = static_root + uri
    return StreamingHttpResponse(file_iterator(file_name))

def version(request):
    file_name = static_root + 'pack.version'
    with open(file_name) as f:
        c = f.read()
    return HttpResponse(c)
