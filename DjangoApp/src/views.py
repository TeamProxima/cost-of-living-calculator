from django.shortcuts import redirect,render
from django.template import RequestContext
from json import dumps, loads, JSONEncoder, JSONDecoder


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
    questions = [{'id': '4444', 'type': 0, 'text': "amina koyyim", 'alt':['DENEME', 'DENEME1']},
          {'id': '445', 'type': 1, 'text': "rack city bitch", 'alt': ['']},
          {'id': '22', 'type': 2, 'text': "yeni bir soru daha", 'alt':['BENI SEC', 'BENI DE SEC']},
          {'id': '3333', 'type': 3, 'text': "sliderini kullan", 'range': range(6)},
          {'id': '222', 'type': 4, 'text': "BUNLAR DA CHECKBOX", 'alt':['gelsin', 'gelmesin']}
          ]

    try:
        if request.META['HTTP_REFERER'].split('/')[-1] == '':
            '''For country and city selection after index'''
            country = request.GET['country']
            city = request.GET['city']
        return render(request, 'questions.html',
                    {'message': '',
                    'questions': questions})
    except Exception as e:
        print e
        return redirect("/")