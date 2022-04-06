import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams


s = requests.Session()
site = 'http://www.hubertiming.com/results/2017GPTR10K'
resp = s.get(site)
soup = BeautifulSoup(resp.text,'html.parser')
rows = soup.find_all('tr')

for row in rows:
    row_td = row.find_all('td')
    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
df = pd.DataFrame(list_rows)
df1 = df[0].str.split(',', expand=True)
df1[0] = df1[0].str.strip('[')
col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
df2 = pd.DataFrame(all_header)
df3 = df2[0].str.split(',', expand=True)
frames = [df3, df1]
df4 = pd.concat(frames)
# print(df4.head(10))
df5 = df4.rename(columns=df4.iloc[0])
# print(df5.head())
# print(df5.info())
# print(df5.shape)
df6 = df5.dropna(axis=0, how='any')
df7 = df6.drop(df6.index[0])
# print(df7.head())
df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team]': 'Team'},inplace=True)
df7['Team'] = df7['Team'].str.strip(']')
# print(df7.head())
time_list = df7[' Chip Time'].tolist()
time_mins = []
for i in time_list:
    if len(i.split(':')) == 2:
        h = 0
        m, s = i.split(':')
    else:
        h, m , s = i.split(':')
    math = (int(h) * 3600 + int(m) * 60 + int(s))/60
    time_mins.append(math)
print(time_mins)
df7['Runner_mins'] = time_mins
print(df7.head())
df7.describe(include=[np.number])
rcParams['figure.figsize'] = 15, 5

df7.boxplot(column='Runner_mins')
plt.grid(True, axis='y')
plt.ylabel('Chip Time')
plt.xticks([1], ['Runners'])
x = df7['Runner_mins']
ax = sns.distplot(x, hist=True, kde=True, rug=False, color='m', bins=25, hist_kws={'edgecolor':'black'})
plt.show()
f_fuko = df7.loc[df7[' Gender']==' F']['Runner_mins']
m_fuko = df7.loc[df7[' Gender']==' M']['Runner_mins']
sns.distplot(f_fuko, hist=True, kde=True, rug=False, hist_kws={'edgecolor':'black'}, label='Female')
sns.distplot(m_fuko, hist=False, kde=True, rug=False, hist_kws={'edgecolor':'black'}, label='Male')
plt.legend()

df7.boxplot(column='Runner_mins', by=' Gender')
plt.ylabel('Chip Time')
plt.suptitle("")


