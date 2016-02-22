#!/usr/bin/env python

"""
This file extracts all country-city pairs from http://www.numbeo.com/cost-of-living/
"""

import requests
import AdvancedHTMLParser
import json
import re


parser = AdvancedHTMLParser.AdvancedHTMLParser()

def readHTML(url):
    r = requests.get(url)
    return r.content


def parseCountries(doc):
    parser.parseStr(doc)
    items = parser.getElementById("country")
    dic = {}
    items = items[1:]
    for item in items:
        dic[item.innerHTML] = []
    return dic

def parseCities(country):
    url = "http://www.numbeo.com/cost-of-living/country_result.jsp?country="+country
    r = readHTML(url)
    parser.parseStr(r) 
    items = parser.getElementById("city")
    l = []
    items = items[1:]
    for item in items:
        l.append(item.innerHTML.encode('ascii', 'ignore'))
    return l

def saveCities():
    url = "http://www.numbeo.com/cost-of-living/"
    doc = readHTML(url)
    countries = parseCountries(doc)

    print "Beginning..."

    for country in countries:
        city_list = parseCities(country)
        print "Parsing done for", country
        countries[country] = city_list

    with open("countries.json", "w") as out:
        out.write(json.dumps(countries, sort_keys=True, indent=4, separators=(',', ': ')))

    print "Aaaand we are done."

def parseCityData(country, city):
    base_url = "http://www.numbeo.com/cost-of-living/country_result.jsp"
    params = {'country': country, 'city': city}
    response = requests.get(base_url, params=params)
    parser.parseStr(response.content)

    prices = []
    table = parser.getElementsByClassName('data_wide_table')
    for tr in table[0]:
        if tr.getElementsByClassName('priceValue'):
            if tr.getElementsByClassName('priceValue') == '?':
                prices.append(None)
            else:
                print tr.getChildren()[1].innerHTML.replace(',','')
                prices.append(float(re.findall("[-+]?\d*\.\d+|\d+", tr.getChildren()[1].innerHTML.replace(',',''))[0]))

    return prices



def saveData():

    with open("cities.json", "r") as f:
        countries = json.loads(f.read())

    with open("props.json", "r") as f:
        props = json.loads(f.read())

    print "Beginning..."

    for country in countries:
        for city in country:
            city_list = parseCityData(country, city)
            print "Parsing done for", country
            countries[country] = city_list

    

    print "Aaaand we are done."


if __name__ == "__main__":
    saveCities()
    # print parseCityData('Turkey', 'Ankara')