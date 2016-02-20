#!/usr/bin/env python

import json
import requests
from AdvancedHTMLParser import AdvancedHTMLParser

# http://www.numbeo.com/cost-of-living/city_result.jsp?country=Turkey&city=Ankara
params = {'country': 'Turkey', 'city': 'Ankara'}
base_url = 'http://www.numbeo.com/cost-of-living/city_result.jsp'
response = requests.get(base_url, params=params)

parser = AdvancedHTMLParser()
parser.parseStr(response.text)

props = []
tmp = parser.getElementsByClassName('data_wide_table')
for tr in tmp[0]:
    if tr.getElementsByClassName('priceValue'):
        # print tr.getChildren()[0].innerHTML.replace('&amp;','&') + tr.getChildren()[1].innerHTML.replace('&nbsp;',' ')
        props.append(tr.getChildren()[0].innerHTML.replace('&amp;','&'))

with open("props.json", "w") as out:
        out.write(json.dumps(props, sort_keys=True, indent=4, separators=(',', ': ')))



