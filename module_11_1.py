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

url1 = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2001&date_req2=14/03/2001&VAL_NM_RQ=R01235'
data = pd.read_xml(url1)
data = data.drop(['Id', 'Nominal', 'VunitRate'], axis='columns')
data1 = data.drop(['Date'], axis='columns')
df = pd.DataFrame(data)
df_melted = df.melt()
print(df_melted)
fig, ax = plt.subplots()
ax.plot()
# print(data1)
# plt.show()
print()

# 5: pillow
import PIL
