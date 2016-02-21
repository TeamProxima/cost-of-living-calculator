from django.shortcuts import redirect,render
from django.contrib.sessions import *
from django.template import RequestContext
from json import dumps, loads, JSONEncoder, JSONDecoder
import random
import MySQLdb

from functions import *
from models import *


pictures = [
    'http://www.mrwallpaper.com/wallpapers/Golden-Gate-Bridge-1920x1080.jpg',
    'http://cdn.superbwallpapers.com/wallpapers/world/machu-picchu-3709-1920x1200.jpg',
    'http://tremendouswallpapers.com/wp-content/uploads/2014/12/Burj_Al_Arab.jpg',
    'http://www.goodwp.com/images/201212/goodwp.com_26355.jpg',
    'https://wallpaperscraft.com/image/spain_toledo_lights_dusk_hdr_93798_1920x1080.jpg',
    'https://wallpaperscraft.com/image/night_eiffel_tower_paris_france_13648_1920x1080.jpg',
    'https://wallpaperscraft.com/image/new_york_statue_of_liberty_river_evening_28423_1920x1080.jpg',
]


def session_handler(request, new=True):
    if new:
        request.session['page_index'] = 0
        request.session['answer'] = {}
    else:
        del request.session['answer']
        del request.session['page_index']
        return False
    return True


def home(request):
    '''Show country and city selection'''
    try:
        context =  {'message': ''}
        return render(request, 'index.html', context)
    except Exception as e:
        print e
        return redirect("/")


country = None
city = None

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

    global pictures
    questions = [{'id': 'mealQ1', 'type': 4, 'text': "What meals do you have?", 'alt':['Breakfast', 'Launch', 'Dinner']},
          {'id': 'mealQ2', 'type': 3, 'text': "What is your preference for meal?", 'range': range(101), 'alt':['Vegetable', 'Meat']},
          {'id': 'mealQ3', 'type': 1, 'text': "How often do you go out for meal?", 'alt':['times a week.']},
          {'id': 'mealQ4', 'type': 3, 'text': "What do you prefer?", 'range': range(101), 'alt': ['Restaurant', 'Fast Food']}
          ]
    questions2 = [{'id': 'beer_cigQ1', 'type': 1, 'text': "How many bottles of beer do you drink per week?", 'alt':[' ']},
          {'id': 'beer_cigQ2', 'type': 1, 'text': "How many packets of cigarette do you smoke per week?", 'alt':[' ']}
          ]

    qlist = [questions, questions2]
    try:
        global country,city
        if request.META['HTTP_REFERER'].split('/')[-1] == '':
            '''For country and city selection after index'''
            country = request.GET['country']
            city = request.GET['city'] 
            session_handler(request)

        if request.POST:
            request.session['page_index'] += 1
            request.session['answer'].update((request.POST.iterlists()))

        return render(request, 'questions.html',
            {'message': '',
             'piclink': pictures[random.randint(0,6)],
            'questions': qlist[request.session['page_index']]})
    except IndexError:
        global country,city
        answers = request.session['answer']
        num_of_beer = int(str(answers['beer_cigQ1'][0]))
        num_of_cig = int(str(answers['beer_cigQ2'][0]))
        meal_list = answers['mealQ1']
        meals = []
        for each in meal_list:
            meals.append(str(each))
        print meals
        veg_ratio = 1-(int(str(answers['mealQ2'][0]))/100.0)
        num_of_out_meal = int(str(answers['mealQ3'][0]))
        restaurant_ratio = 1- (int(str(answers['mealQ4'][0]))/100.0)
        print veg_ratio, num_of_out_meal, restaurant_ratio
        
        print 'nums beer cig:', num_of_beer, num_of_cig
         
        for key,value in answers.iteritems():
            print key, value
        db = MySQLdb.connect("localhost","root","root","test")
        cursor = db.cursor()
        print "select * from info where country='"+country+"' and city='"+city+"';"
        cursor.execute("select * from info where country='"+country+"' and city='"+city+"';")
        data = cursor.fetchone()
        print data
        db.close()
        
        daily_cost = meal_cost(meals, veg_ratio, num_of_out_meal, restaurant_ratio, data[2:])
        print 'cost',daily_cost
        
        '''
            'answers' has answers as a dictionary.
            Finished, calculate.
        '''
        session_handler(request, False)
        return redirect("/")
    except Exception as e:
        print e
        return redirect("/")
