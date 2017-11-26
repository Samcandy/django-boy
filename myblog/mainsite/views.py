# -*- coding: utf-8 -*-


#from __future__ import unicode_literals # transation ascii code

from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import Post


from datetime import datetime
from django.template.loader import get_template

# Create your views here.

# Get all article context
def homepage(request):

#    posts = Post.objects.all()
#    post_lists = list()
#    for count, post in enumerate(posts):
#        post_lists.append("No.{}:".format(str(count))+ str(post) + "<br>")
#        post_lists.append("<small>" + str(post.body.encode('utf-8','ignore')) + "</small><br><br>")
    template = get_template('index2.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())    # locals() will memory all local variable use dictionary type to package 
        
    #return HttpResponse(post_lists)
    
    return HttpResponse(html)

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')



