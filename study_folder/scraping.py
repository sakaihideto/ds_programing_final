#create a list
climate_list= []

#scraping
import requests
import csv
r=requests.get("https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view=p1")

encoding=r.encoding
if encoding.lower() == 'iso-8859-1':
    r.encoding = 'utf-8'

from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text, 'html.parser')

tag=soup.find('table', id='tablefix1', class_='data2_s')

index=20
# with open("climate.csv", "w", newline="", encoding="utf-8") as csvfile:
            # csv_writer = csv.writer(csvfile)
for row in tag.find_all('tr')[1:]:
    columns=row.find_all('td')
    if columns:
        target_data=columns[index].text
        print(target_data)
        climate_list.append(target_data)
        # with open("climate.csv", "w", newline="", encoding="utf-8") as csvfile:
    # データを書き込み
            # csv_writer = csv.writer(csvfile)
            # for data in target_data:
            # csv_writer.writerows([target_data])
# weather=tag.find_all('td', class_='data_0_0')
# target=([x.string for x in weather])
# print(target)
print(climate_list)
