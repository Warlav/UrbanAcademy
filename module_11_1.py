#1: requests
from pprint import pprint
import requests

r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# print('status code: ', r.status_code)
# print(r.headers['Content-Type'])
#r.content
#r.encoding = 'utf-8'
#print(r.text)
try:
  pprint(r.json()['Valute']['USD'])
except ValueError:
  print('Не удалось преобразовать JSON')
print()

#2: pandas
import pandas as pd

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
curr = pd.read_xml(url, encoding='cp1251')
curr = curr.drop(['ID', 'NumCode', 'VunitRate'], axis='columns')
curr1 = curr.loc[13]
print(curr1)
print()


#3: numpy
import numpy as np

a = np.array(curr)
print(a)
print()

#4: matplotlib
import matplotlib
print()

#5: pillow
import PIL