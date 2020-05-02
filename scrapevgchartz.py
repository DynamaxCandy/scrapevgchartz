from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import urllib.error
import time

pages = 50
rec_count = 0
rank = []
gname = []
console = []
publisher = []
shipped = []
sales_na = []
sales_pal = []
sales_jp = []
sales_ot = []
sales_gl = []
releasedate = []
lastupdate = []




urlhead = 'http://www.vgchartz.com/gamedb/?page='
urltail = 'name=&keyword=&console=&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=10&order=Salesname=&keyword=&console=&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=10&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&shownasales=0&shownasales=1&showdeveloper=0&showcriticscore=0&showpalsales=0&showpalsales=1&showreleasedate=0&showreleasedate=1&showuserscore=0&showjapansales=0&showjapansales=1&showlastupdate=0&showlastupdate=1&showothersales=0&showothersales=1&showshipped=0&showshipped=1'

for page in range(1, pages):
        surl = urlhead + str(page) + urltail
        try:
            r = urllib.request.urlopen(surl).read()
        except urllib.error.HTTPError:
            time.sleep(20)
            r = urllib.request.urlopen(surl).read()


        soup = BeautifulSoup(r, features="lxml")
        print(page)
        chart = soup.find('div', id='generalBody').find('table')
        for row in chart.find_all('tr')[3:]:
                col = row.find_all('td')


                col_1 = col[0].string.strip()
                col_2 = col[2].find('a').string.strip()
                col_3 = col[3].find('img')['alt'].strip()
                col_4 = col[4].string.strip()
                col_5 = col[5].string.strip()
                col_6 = col[6].string.strip()
                col_7 = col[7].string.strip()
                col_8 = col[8].string.strip()
                col_9 = col[9].string.strip()
                col_10 = col[10].string.strip()
                col_11 = col[11].string.strip()

                rank.append(col_1)
                gname.append(col_2)
                console.append(col_3)
                publisher.append(col_4)
                shipped.append(col_5)
                sales_na.append(col_6)
                sales_pal.append(col_7)
                sales_jp.append(col_8)
                sales_ot.append(col_9)
                releasedate.append(col_10)
                lastupdate.append(col_11)

                rec_count += 1





columns = {'Rank': rank,
            'Name': gname,
            'Console': console,
            'Publisher': publisher,
            'Total_shipped': shipped,
            'NA_Sales': sales_na,
            'PAL_Sales': sales_pal,
            'JP_Sales': sales_jp,
            'Other_Sales': sales_ot,
            'Release_Date': releasedate,
            'Last_Date': lastupdate, }

print (rec_count)
df = pd.DataFrame(columns)
print(df)
df = df[['Rank', 'Name', 'Console', 'Publisher',
        'Total_shipped','NA_Sales','PAL_Sales','JP_Sales','Other_Sales',
        'Release_Date','Last_Date',]]
df.to_csv("./vgsales.csv", sep=",", encoding='utf-8')
