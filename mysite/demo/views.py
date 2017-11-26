# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django import template

from django.shortcuts import render

import os

def table(request):
    if 'msg' in request.GET:
        if request.GET['msg'] == 'start':
            res = os.popen('cat ~/work/html/sample.html')
            return HttpResponse(res)    
    else: 
        return render(request, '../templates/index.html')    


