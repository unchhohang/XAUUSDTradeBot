# Program that process history price html raw data to csv

from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np

Datas = []

with open('Data.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for trs in soup.find_all('tr'):
    Datas.append([tds.get_text() for tds in trs if tds != '\n'])

date = [pd.to_datetime(child[0]).strftime('%Y-%m-%d') for child in Datas]
open = [float(child[1].replace(',','')) for child in Datas]
high = [float(child[2].replace(',','')) for child in Datas]
low = [float(child[3].replace(',','')) for child in Datas]
close = [float(child[4].replace(',','')) for child in Datas]
adjClose = [float(child[5].replace(',','')) for child in Datas]
volume = [child[6] for child in Datas ]

df = pd.DataFrame({
    "Date": date,
    "Open": open,
    "High": high,
    "Low": low,
    "Close": close,
    "Adj Close": adjClose,
    "Volume": volume 
})

df['Volume']= df['Volume'].replace('-', np.nan)
df['Volume']= df['Volume'].ffill()


df.to_csv('resultData.csv',index=False)
