from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


console = []
sales_na = []
sales_jp = []
sales_eu = []
sales_ot = []
sales_gl = []

url = 'https://www.vgchartz.com/analysis/platform_totals/Hardware/Global/'
req = urllib.request.Request(url)
r = urllib.request.urlopen(req).read()
soup = BeautifulSoup(r, features="lxml")
parse = soup.find('tbody')
for row in parse.find_all('tr')[0:25]:
    col = row.find_all('td')

    col_1 = col[1].string.strip()
    col_2 = col[2].string.strip()
    col_3 = col[3].string.strip()
    col_4 = col[4].string.strip()
    col_5 = col[5].string.strip()
    col_6 = col[6].string.strip()

    console.append(col_1)
    sales_na.append(col_2)
    sales_eu.append(col_3)
    sales_jp.append(col_4)
    sales_ot.append(col_5)
    sales_gl.append(col_6)

columns = {
            'Console': console,
            'NA_Sales': sales_na,
            'EU_Sales': sales_eu,
            'JP_Sales': sales_jp,
            'Other_Sales': sales_ot,
            'Global_Sales': sales_gl, }

df = pd.DataFrame(columns)
df = df[['Console',
        'NA_Sales','EU_Sales','JP_Sales','Other_Sales',
        'Global_Sales',]]
df.to_csv("./consolesales.csv", sep=",", encoding='utf-8')
