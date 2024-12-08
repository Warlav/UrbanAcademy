# 1: requests
from pprint import pprint
import requests

r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# print('status code: ', r.status_code)
# print(r.headers['Content-Type'])
# r.content
# r.encoding = 'utf-8'
# print(r.text)
try:
    print(r.json()['Valute']['USD'])
    print(r.json()['Valute']['EUR'])
except ValueError:
    print('Не удалось преобразовать JSON')
print()

# 2: pandas
import pandas as pd

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
curr = pd.read_xml(url, encoding='cp1251')
curr = curr.drop(['ID', 'NumCode', 'VunitRate'], axis='columns')
curr_usd = curr.loc[13]
curr_eur = curr.loc[14]
print(f'{curr_usd},\n\n {curr_eur}')
print()

# 3: numpy
import numpy as np

usd = np.array(curr)[13]
eur = np.array(curr)[14]
print(f'{usd},\n{eur}')
print()

# 4: matplotlib
import matplotlib.pyplot as plt

url1 = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=21/11/2024&date_req2=09/12/2024&VAL_NM_RQ=R01235'
data = pd.read_xml(url1)
print(data['Value'])
# data = (data.drop(['Id', 'Nominal', 'VunitRate'], axis='columns'))
fig, axs = plt.subplots()
axs.plot(data['Date'], data['Value'].T)
plt.show()
print()

# 5: pillow
import PIL
