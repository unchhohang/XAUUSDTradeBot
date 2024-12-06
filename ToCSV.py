# Program that process history price html raw data to csv

from bs4 import BeautifulSoup 
import pandas as pd 

Datas = []

with open('Data.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for trs in soup.find_all('tr'):
    Datas.append([tds.get_text() for tds in trs if tds != '\n'])

date = [pd.to_datetime(child[0]).strftime('%y-%m-%d') for child in Datas]
open = [child[1] for child in Datas]
high = [child[2] for child in Datas]
low = [child[3] for child in Datas]
close = [child[4] for child in Datas]
adjClose = [child[5] for child in Datas]
volume = [child[6] for child in Datas]

df = pd.DataFrame({
    "Date": date,
    "Open": open,
    "High": high,
    "Low": low,
    "Close": close,
    "Adj Close": adjClose,
    "Volume": volume
})

df.to_csv('resultData.csv',index=False)
