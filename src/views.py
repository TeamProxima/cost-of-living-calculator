from django.shortcuts import redirect,render
from django.contrib.sessions import *
from django.template import RequestContext
from json import dumps, loads, JSONEncoder, JSONDecoder
from django.http import JsonResponse
import random
import MySQLdb
import requests
import json
from walrus import *
from functions import *
from models import *

uberClientId = "cmyl27bKm6lbKhvCHcBOX5Rz2c4Fy8Y"
uberServerToken = "85bCl3jLGRsYnWM9hcGfrmLk4Zteg49Nvn3ga_hw"

currency_dict = {u'Canada': u'C$', u'Maldives': u'Rf', u'Turkmenistan': u'&#36;', u'Saint Helena': u'&#163;', u'Lithuania': u'&#8364;', u'Cambodia': u'&#36;', u'Ethiopia': u'&#36;', u'Aruba': u'&#36;', u'Swaziland': u'R', u'Argentina': u'&#36;', u'Bolivia': u'Bs.', u'Cameroon': u'&#36;', u'Burkina Faso': u'CFA', u'Ghana': u'&#36;', u'Saudi Arabia': u'&#65020;', u'Myanmar': u'&#36;', u'Cape Verde': u'Esc', u'Slovenia': u'&#8364;', u'Guatemala': u'Q', u'Germany': u'&#8364;', u'Dominica': u'EC$', u'Australia': u'A$', u'Liberia': u'&#36;', u'Kosovo (Disputed Territory)': u'&#8364;', u'Pakistan': u'Rs.', u'Oman': u'&#65020;', u'Tanzania': u'&#36;', u'Palestinian Territory': u'&#8362;', u'Saint Kitts And Nevis': u'&#36;', u'Albania': u'Lek', u'Gabon': u'CFA', u'Monaco': u'&#8364;', u'Bahamas': u'&#36;', u'New Zealand': u'NZ$', u'Yemen': u'&#36;', u'Jersey': u'&#163;', u'Jamaica': u'J$', u'Greenland': u'kr', u'Samoa': u'WST', u'United Arab Emirates': u'AED', u'Guam': u'&#36;', u'India': u'Rs', u'Azerbaijan': u'&#1084;&#1072;&#1085;', u'Madagascar': u'&#36;', u'Lesotho': u'R', u'Saint Vincent And The Grenadines': u'EC$', u'Kenya': u'KSh', u'South Korea': u'&#8361;', u'Tajikistan': u'SM', u'Turkey': u'TL', u'Afghanistan': u'&#36;', u'Northern Mariana Islands': u'&#36;', u'Eritrea': u'&#8364;', u'Solomon Islands': u'SI$', u'Saint Lucia': u'EC$', u'Kyrgyzstan': u'&#36;', u'Mongolia': u'&#36;', u'France': u'&#8364;', u'Bermuda': u'&#36;', u'Slovakia': u'&#8364;', u'Somalia': u'&#36;', u'Peru': u'S/.', u'Laos': u'&#36;', u'Norway': u'kr', u'Malawi': u'&#36;', u'Cook Islands': u'NZ$', u'Western Sahara': u'MAD', u'Cuba': u'&#36;', u'Montenegro': u'&#8364;', u'Togo': u'CFA', u'China': u'&#165;', u'Armenia': u'AMD', u'Dominican Republic': u'RD$', u'Ukraine': u'&#36;', u'Bahrain': u'BHD', u'Tonga': u'T$', u'Finland': u'&#8364;', u'Libya': u'LD', u'Indonesia': u'Rp', u'Mauritius': u'Rs', u'Liechtenstein': u'Fr.', u'Vietnam': u'&#8363;', u'Antigua And Barbuda': u'EC$', u'Mali': u'&#36;', u'Russia': u'&#8364;', u'Bulgaria': u'&#1083;&#1074;', u'United States': u'&#36;', u'Romania': u'lei', u'Angola': u'&#36;', u'Cayman Islands': u'&#36;', u'South Africa': u'R', u'Macao': u'P', u'Sweden': u'kr', u'Malaysia': u'RM', u'Austria': u'&#8364;', u'Mozambique': u'MT', u'Uganda': u'USh', u'Japan': u'&#165;', u'Niger': u'CFA', u'Brazil': u'R$', u'Faroe Islands': u'kr', u'Kuwait': u'KWD', u'Panama': u'&#36;', u'Guyana': u'&#36;', u'Costa Rica': u'&#8353;', u'Luxembourg': u'&#8364;', u'Andorra': u'&#8364;', u'British Virgin Islands': u'&#36;', u'Gibraltar': u'&#163;', u'Ivory Coast': u'CFA', u'Nigeria': u'&#8358;', u'Ecuador': u'&#36;', u'Bangladesh': u'&#2547;', u'Brunei': u'S$', u'Belarus': u'&#36;', u'Iran': u'&#36;', u'Algeria': u'DZD', u'El Salvador': u'&#36;', u'Czech Republic': u'K\u010d', u'Marshall Islands': u'&#36;', u'Chile': u'CL$', u'Puerto Rico': u'&#36;', u'Belgium': u'&#8364;', u'Thailand': u'&#3647;', u'Haiti': u'&#36;', u'Belize': u'&#36;', u'Hong Kong': u'HK$', u'Georgia': u'GEL', u'Gambia': u'D', u'Philippines': u'&#8369;', u'Sao Tome And Principe': u'&#8364;', u'Namibia': u'R', u'Moldova': u'L', u'Portugal': u'&#8364;', u'Morocco': u'MAD', u'Croatia': u'kn', u'French Polynesia': u'&#8364;', u'Guernsey': u'&#163;', u'Switzerland': u'Fr.', u'Grenada': u'EC$', u'Seychelles': u'&#8360;', u'Chad': u'CFA', u'Estonia': u'&#8364;', u'Uruguay': u'$U', u'Equatorial Guinea': u'CFA', u'Lebanon': u'&#36;', u'Uzbekistan': u'&#36;', u'Egypt': u'EG&#163;', u'Djibouti': u'Fdj', u'Rwanda': u'RF', u'Timor-Leste': u'&#36;', u'Spain': u'&#8364;', u'Colombia': u'Col$', u'Reunion': u'&#8364;', u'Burundi': u'&#36;', u'Taiwan': u'NT$', u'Cyprus': u'&#8364;', u'Barbados': u'Bds$', u'Us Virgin Islands': u'&#36;', u'Qatar': u'QR', u'Isle Of Man': u'&#163;', u'Italy': u'&#8364;', u'Curacao': u'NAf', u'Bhutan': u'Rs', u'Sudan': u'&#36;', u'Nepal': u'N&#8360;', u'Micronesia': u'&#36;', u'Netherlands': u'&#8364;', u'Bosnia And Herzegovina': u'KM', u'Suriname': u'SRD', u'Venezuela': u'&#36;', u'Aland Islands': u'&#8364;', u'Israel': u'&#8362;', u'Turks And Caicos Islands': u'&#36;', u'Zambia': u'ZMW', u'Senegal': u'CFA', u'Papua New Guinea': u'&#36;', u'Zimbabwe': u'&#36;', u'Jordan': u'JOD', u'Vanuatu': u'VT', u'Denmark': u'kr', u'Kazakhstan': u'&#1083;&#1074;', u'Poland': u'&#122;&#322;', u'Mauritania': u'UM', u'Ireland': u'&#8364;', u'Iraq': u'&#36;', u'Greece': u'&#8364;', u'New Caledonia': u'F', u'Macedonia': u'&#1076;&#1077;&#1085;', u'Paraguay': u'Gs', u'Latvia': u'&#8364;', u'South Sudan': u'&#36;', u'Hungary': u'Ft', u'Syria': u'&#36;', u'Sint Maarten': u'&#36;', u'Honduras': u'&#36;', u'Malta': u'&#8364;', u'Mexico': u'MXN', u'Tunisia': u'DT', u'Nicaragua': u'&#36;', u'Singapore': u'S$', u'Serbia': u'&#1044;&#1080;&#1085;', u'United Kingdom': u'&#163;', u'Trinidad And Tobago': u'TT$', u'Congo': u'&#8364;', u'Iceland': u'kr', u'Sri Lanka': u'Rs', u'Fiji': u'FJ$', u'Botswana': u'P'}

'''
def maps(city, country):
    address = city+" "+country
    path = "http://maps.googleapis.com/maps/api/geocode/json?address="+address+"&sensor=false"
    result = requests.post(path)
    result = result.content
    d = json.loads(result)
    if d['status'] == 'OK': 
        n_values = d['results'][0]['geometry']['bounds']['northeast']
        n_lat, n_lng = n_values['lat'], n_values['lng']
        s_values = d['results'][0]['geometry']['bounds']['southwest']
        s_lat, s_lng = s_values['lat'], s_values['lng']
        return (n_lat, n_lng, s_lat, s_lng)

def uber(loc):
    path = "https://api.uber.com/v1/products"
    headers = {
        'Authorization': "Token " + uberServerToken
    }
    data = { 
      'latitude': (loc[0] + loc[2]) / 2,
      'longitude': (loc[1] + loc[3]) / 2
     # 'end_latitude':loc[2],
      #'end_longitude':loc[3]
    }

    r = requests.get(path, headers=headers, params=data)
    return r

def gouber(country, city):
    info = maps(city,country)
    #print info
    res = uber(info)
    print 'res', res
    d =  json.loads(res.text)
    for each in d['products']:
        if eac1h['display_name'] == 'uberX':
            p = each['price_details']
            base = p['base']
            cost = p['cost_per_distance']
            return [base,cost]
        else:
            return [-1,-1]
            
   '''                 
        

def search(request):
    database = Database()
    ac = database.autocomplete()
    # print request.GET['term']
    city_list = list(ac.search(request.GET['term']))
    #print city_list
    city_list = city_list[:3]
    city_dict = {}
    for i in range(len(city_list)):
        # city_dict[str(i)] = {'country': city_list[i]['country'], 'city': city_list[i]['city']}
        city_dict[str(i)] = {'label': city_list[i]['city'], 'desc': city_list[i]['country']}
    #print city_dict
    try:
        return JsonResponse(city_dict)
    except Exception as e:
        print "Exception",e


def session_handler(request, new=True):
    if new:
        request.session['country'] = request.GET['country']
        request.session['city'] = request.GET['city']
        request.session['currency'] = currency_dict[request.GET['country']]
        print request.session['country'], request.session['city']
        request.session['page_index'] = 0
        request.session['answer'] = {}
    else:
        del request.session['country']
        del request.session['city']
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

def calculate(request, answers):
    country = request.session['country']
    city = request.session['city']
    num_of_beer = int(str(answers['beer_cigQ1'][0]))
    num_of_cig = int(str(answers['beer_cigQ2'][0]))
    meal_list = answers['mealQ1']
    meals = []
    for each in meal_list:
        meals.append(str(each))
    #print meals
    veg_ratio = 1-(int(str(answers['mealQ2'][0]))/100.0)
    num_of_out_meal = int(str(answers['mealQ3'][0]))
    restaurant_ratio = 1- (int(str(answers['mealQ4'][0]))/100.0)
    #print veg_ratio, num_of_out_meal, restaurant_ratio
    #print 'nums beer cig:', num_of_beer, num_of_cig
    #for key,value in answers.iteritems():
    #    print key, value
    home_choice = str(answers['accoQ1'][0])
    num_of_bedroom = int(str(answers['accoQ2'][0]))
    pieces_per_month = int(str(answers['miscQ1'][0]))
    cinema = int(str(answers['miscQ2'][0]))
    gym = str(answers['miscQ3'][0])
    miles_per_week = int(str(answers['transQ1'][0]))
    times_of_public = int(str(answers['transQ2'][0]))
    times_of_taxi =  int(str(answers['transQ3'][0]))
    db = MySQLdb.connect("localhost","root","root","test")
    cursor = db.cursor()
    #print "select * from info where country='"+country+"' and city='"+city+"';"
    cursor.execute("select * from info where country='"+country+"' and city='"+city+"';")
    data = cursor.fetchone()
    #print data
    db.close()

    beer_cig = beer_cigarette_cost(num_of_beer,num_of_cig, data[2:])
    beer, cig, total1 = beer_cig['Beer'], beer_cig['Cigarette'], beer_cig['Total']
    
    food_cost = meal_cost(meals, veg_ratio, num_of_out_meal, restaurant_ratio, data[2:])
    breakfast, lunch, dinner, fruit, total2 = food_cost['Breakfast'], food_cost['Lunch'], food_cost['Dinner'], food_cost['Fruit'], food_cost['Total']

    accomodation_cost = accomodation_cost36(home_choice,num_of_bedroom,data[2:])
    utilities_cost = utilities_cost36(num_of_bedroom,data[2:])
    total0 = accomodation_cost + utilities_cost
    accomodation_cost2 = {'Rent':accomodation_cost, 'Utilities': utilities_cost, 'Total':total0}
    misc_cost = misc_cost36(pieces_per_month, cinema, gym, data[2:])
    outfit, cinema, fitness, total3 = misc_cost['Outfit'],misc_cost['Cinema'],misc_cost['Fitness'],misc_cost['Total']
    
    
    #uber = gouber(country, city)
    
    transportation_cost = transportation_cost36(miles_per_week, times_of_public, times_of_taxi,-1,-1, data[2:])
    public, taxi, drive, total4 = transportation_cost['Public_Trans'],transportation_cost['Taxi_Total'],transportation_cost['Drive_Total'],transportation_cost['Total']
    
    total_cost = total1 + total2 + total3 + total4 + total0
    return {'totalCost':total_cost, 'foodCost':food_cost, 'accomodationCost':accomodation_cost2, 
            'tobacco':beer_cig, 'miscCost':misc_cost,
            'transportationCost':transportation_cost, 'currency':request.session['currency'],
            #'uber': {'base':uber[0], 'price':uber[1]}
            }


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
    questions = [{'id': 'mealQ1', 'type': 4, 'text': "Which meals do you eat?", 'alt':['Breakfast', 'Launch', 'Dinner'], 'info':['Please indicate which meals you wish to eat.']},
          {'id': 'mealQ2', 'type': 3, 'text': "What do you prefer in a meal?", 'range': range(101), 'alt':['Vegetable', 'Meat'], 'info':['Please indicate a close ratio of vegetables over meat in your meals. Note that the percantage is to show ratio for meat.']},
          {'id': 'mealQ3', 'type': 1, 'text': "How often do you go out for a meal?", 'alt':['times a week'],'info':['Please tell us how many times you go out per week for a meal, include orders to your place.']},
          {'id': 'mealQ4', 'type': 3, 'text': "What do you prefer?", 'range': range(101), 'alt': ['Restaurant', 'Fast Food'],' info':['Please indicate a close ratio of the food you eat from a restaurant over fast food places includes orders to your place.']}
          ]
    questions2 = [{'id': 'beer_cigQ1', 'type': 1, 'text': "How much beer do you drink?", 'alt':['bottles per week'],' info':['Please tell us a close number of beers you drink per week. One bottle of beer is 500ml']},
          {'id': 'beer_cigQ2', 'type': 1, 'text': "How many cigarette do you smoke?", 'alt':['packets per week'],' info':['Please tell us the number of cigarette packets you buy.']}
          ]
    questions3 = [{'id': 'accoQ1', 'type': 0, 'text': "Where do you want to live?", 'alt':['In city centre', 'Outside of city centre'],' info':['Please tell us if you want to live in city centre or not.']},
          {'id': 'accoQ2', 'type': 0, 'text': "How many bedrooms?", 'alt':['1', '2', '3'],' info':['Please tell us how many bedrooms you want in your house.']}
          ]
    questions4 = [{'id': 'transQ1', 'type': 1, 'text': "How many miles do you drive?", 'alt':['miles per week'],'info':['Please tell us approximate number of miles you drive per week. If you do not have a car please give 0.']},
          {'id': 'transQ2', 'type': 1, 'text': "How many times do you use public transportation?", 'alt':['times a week'],'info':['Please tell us how many times you use public transportation per week approximately. Note that you need to count round trip transportation as 2.']},
          {'id': 'transQ3', 'type': 1, 'text': "How many times do you use taxi or uber?", 'alt':['times a week'], 'info':['Please tell us approximate number of taking taxi per week. Note that in our calculations, 7 miles is average distance for single drive. You can consider this information to give your approximate number.']}
          ]
    questions5 = [{'id': 'miscQ1', 'type': 1, 'text': "How many pieces of outfit do you buy?", 'alt':['pieces per month'], 'info':['Please tell us average number of outfits you buy per month.']},
          {'id': 'miscQ2', 'type': 1, 'text': "How often do you go to cinema?", 'alt':['times a month'], 'info':['Please tell us how many times you go to cinema per month.']},
          {'id': 'miscQ3', 'type': 0, 'text': "Do you want to have gym membership?", 'alt':['Yes', 'No'], 'info':['Please tell us if you would like to have monthly gym membership.']}
          ]

    qlist = [questions, questions2, questions3, questions4, questions5]
    try:
        if request.META['HTTP_REFERER'].split('/')[-1] == '':
            '''For country and city selection after index'''
            
            session_handler(request)

        if request.POST:
            request.session['page_index'] += 1
            request.session['answer'].update((request.POST.iterlists()))
            print request.session['answer']

        return render(request, 'questions.html',
            {'message': '',
             'piclink': "pics/" + str(random.randint(0, 6)) + ".jpg",
            'questions': qlist[request.session['page_index']],
             'page_headers': [request.session['country'], request.session['city']]
             })
    except IndexError:
        answers = request.session['answer']
        cost_dict = calculate(request, answers)
        request.session['cost'] = cost_dict
        '''
        'answers' has answers as a dictionary.
        Finished, calculate.
        '''
        session_handler(request, False)
        #return redirect("/")
        return render(request, 'result.html', request.session['cost'])
    except Exception as e:
        print  e
        return redirect("/")
