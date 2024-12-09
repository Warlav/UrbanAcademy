# 1: requests
from pprint import pprint

import matplotlib
import requests

r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
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

url1 = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/11/2024&date_req2=09/12/2024&VAL_NM_RQ=R01235'
data = pd.read_xml(url1)
plt.plot(data['Date'], list(map(float, data['Value'].str.replace(',', '.').tolist())))
plt.xticks(rotation=45, fontsize=6)
plt.title('Курс доллара', fontsize=15)
plt.show()
print()

# 5: pillow
from PIL import Image, ImageOps

size = (256, 256)
with Image.open('PingPong/ball.png') as ball:
    print(ball.size)
    ImageOps.cover(ball, size).save('PingPong/ball_cover.png')

with Image.open('PingPong/ball_cover.png') as im:
    print(im.size)
