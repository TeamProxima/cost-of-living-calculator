from django.shortcuts import redirect,render
from django.template import RequestContext
from json import dumps, loads, JSONEncoder, JSONDecoder

from models import *

import MySQLdb

def home(request):
    '''Show country and city selection'''
    try:
        context =  {'message': ''}
        return render(request, 'index.html', context)
    except Exception as e:
        print e
        return redirect("/")


def run(request):
    '''Ask questions to calculate price'''
    '''
        Question Format
        ID: Unique question identifier to evaluate answers
        Type: Identifier to determine question format
            Radio Button: 0
            Text Input: 1
            Dropdown: 2
            Slider: 3
            Checkbox: 4
        Text: Question text
        Alternative: Radio button, checkbox, dropdown alternatives
        Range: Slider range

    '''

    questions = [{'id': 'mealQ1', 'type': 4, 'text': "What meals do you have?", 'alt':['Breakfast', 'Launch', 'Dinner']},
          {'id': 'mealQ2', 'type': 3, 'text': "What is your preference for meal?", 'range': range(100), 'alt':['Vegetable', 'Meat']},
          {'id': 'mealQ3', 'type': 1, 'text': "How often do you go out for meal?", 'alt':['times a week']},
          {'id': 'mealQ4', 'type': 3, 'text': "What do you prefer?", 'range': range(100), 'alt': ['Restaurant', 'Fast Food']}
          ]
    questions2 = [{'id': 'beer_cigQ1', 'type': 1, 'text': "How many bottles of beer do you drink per week?", 'alt':[' ']},
          {'id': 'beer_cigQ2', 'type': 1, 'text': "How many packets of cigarette do you smoke per week?", 'alt':[' ']}
          ]

    qlist = [questions, questions2]
    page_index = 0
    try:
        if request.META['HTTP_REFERER'].split('/')[-1] == '':
            '''For country and city selection after index'''
            country = request.GET['country']
            city = request.GET['city']
            db = MySQLdb.connect("localhost","root","root","test")
            cursor = db.cursor()
            print "select * from info where country='"+country+"' and city='"+city+"';"
            cursor.execute("select * from info where country='"+country+"' and city='"+city+"';")
            data = cursor.fetchone()
            print data
            db.close()
        if request.POST:
            page_index += 1
            print request.POST
        print page_index
        return render(request, 'questions.html',
                    {'message': '',
                    'questions': qlist[page_index]})
    except Exception as e:
        print e
        return redirect("/")
        page_index = 0
        return redirect("/")
