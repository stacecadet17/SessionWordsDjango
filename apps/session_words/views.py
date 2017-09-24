# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime

# Create your views here.
def index(request):
    if "print_words" not in request.session: #initializes variable to hold words in session
        request.session["print_words"] = []
    return render(request, "session_words/index.html") # displays the index html automatically

def add(request):
    if len (request.POST['word']) < 1: #make sure that a word is typed in
        return redirect('/')
    if "size" in request.POST: #if make font bigger is selected.. print size as 50
        size = '50px'
    else:
        size = '20px'

    if 'color' in request.POST: #if a color option is selected, print it as the color that was requested
        color = request.POST['color']
    else:
        color = 'black'

    print_words = request.session['print_words'] #print_words equals whatever word is typed into the text entry field
    print_words.append({
        "word": request.POST['word'],
        "color": color,
        "size": size,
        "time": strftime('%I:%M:%S %p, %B %d, %Y', localtime()),
        })
    request.session['print_words'] = print_words #update what print_words has become
    return redirect('/')

def clear(request):
    request.session.clear() #end the session 
    return redirect('/')
