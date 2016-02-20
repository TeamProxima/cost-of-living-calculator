from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions import *
from django.http import HttpResponse
from json import dumps, loads, JSONEncoder, JSONDecoder
from datetime import datetime
from random import randint
from .models import *

import time


def home(request):
    '''Show country and city selection'''
    try:
        context =  {'message': ''}
        return render(request, 'index.html', context)
    except Exception as e:
        print e
        return redirect("/home")


def run(request):
    '''Ask questions to calculate price'''
    try:
        country = request.GET['country']
        city = request.GET['city']
        print country, city

        return render(
            request, 'questions.html',
            {'message':'CAT1',
             'questions':[{'type': 0, 'text': "amina koyyim", 'alt':['DENEME', 'DENEME1']},
                          {'type': 2, 'text': "yeni bir soru daha", 'opt':['BENI SEC', 'BENI DE SEC']},
                          {'type': 1, 'text': "rack this bitch"}]})
    except Exception as e:
        print e
        return redirect("/home")