
#October 25
import requests
from bs4 import BeautifulSoup
October_25_url= 'https://www.basketball-reference.com/boxscores/?month=10&day=25&year=2022'
r= requests.get(October_25_url)
soup= BeautifulSoup(r.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Oct_25_EC= tables[0]
Oct_25_WC= tables[1]
Oct_25_EC_Standings=[]
Oct_25_WC_Standings=[]
for team in Oct_25_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Oct_25_EC_Standings.append(EC_team)
for team in Oct_25_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Oct_25_WC_Standings.append(WC_team)



#November 1

November_1st_url= 'https://www.basketball-reference.com/boxscores/?month=11&day=1&year=2022'
r2= requests.get(November_1st_url)
soup= BeautifulSoup(r2.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Nov_1_EC= tables[0]
Nov_1_WC= tables[1]
Nov_1_EC_Standings=[]
Nov_1_WC_Standings= []
for team in Nov_1_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_1_EC_Standings.append(EC_team)
for team in Nov_1_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_1_WC_Standings.append(WC_team)

#November 8

November_8_url= 'https://www.basketball-reference.com/boxscores/?month=11&day=8&year=2022'
r3= requests.get(November_8_url)
soup= BeautifulSoup(r3.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Nov_8_EC= tables[0]
Nov_8_WC= tables[1]
Nov_8_EC_Standings=[]
Nov_8_WC_Standings= []
for team in Nov_8_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_8_EC_Standings.append(EC_team)
for team in Nov_8_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_8_WC_Standings.append(WC_team)

#November 15

November_15_url= 'https://www.basketball-reference.com/boxscores/?month=11&day=15&year=2022'
r4= requests.get(November_15_url)
soup= BeautifulSoup(r4.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Nov_15_EC= tables[0]
Nov_15_WC= tables[1]
Nov_15_EC_Standings=[]
Nov_15_WC_Standings= []
for team in Nov_15_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_15_EC_Standings.append(EC_team)
for team in Nov_15_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_15_WC_Standings.append(WC_team)

#November 22

November_22_url= 'https://www.basketball-reference.com/boxscores/?month=11&day=22&year=2022'
r5= requests.get(November_22_url)
soup= BeautifulSoup(r5.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Nov_22_EC= tables[0]
Nov_22_WC= tables[1]
Nov_22_EC_Standings=[]
Nov_22_WC_Standings= []
for team in Nov_22_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_22_EC_Standings.append(EC_team)
for team in Nov_22_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_22_WC_Standings.append(WC_team)

#November 29

November_29_url= 'https://www.basketball-reference.com/boxscores/?month=11&day=29&year=2022'
r6= requests.get(November_29_url)
soup= BeautifulSoup(r6.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Nov_29_EC= tables[0]
Nov_29_WC= tables[1]
Nov_29_EC_Standings=[]
Nov_29_WC_Standings= []
for team in Nov_29_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_29_EC_Standings.append(EC_team)
for team in Nov_29_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Nov_29_WC_Standings.append(WC_team)

#December 6

December_6_url= 'https://www.basketball-reference.com/boxscores/?month=12&day=6&year=2022'
r7= requests.get(December_6_url)
soup= BeautifulSoup(r7.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Dec_6_EC= tables[0]
Dec_6_WC= tables[1]
Dec_6_EC_Standings=[]
Dec_6_WC_Standings= []
for team in Dec_6_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Dec_6_EC_Standings.append(EC_team)
for team in Dec_6_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Dec_6_WC_Standings.append(WC_team)

#December 13
December_13_url= 'https://www.basketball-reference.com/boxscores/?month=12&day=13&year=2022'
r8= requests.get(December_13_url)
soup= BeautifulSoup(r8.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Dec_13_EC= tables[0]
Dec_13_WC= tables[1]
Dec_13_EC_Standings=[]
Dec_13_WC_Standings= []
for team in Dec_13_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Dec_13_EC_Standings.append(EC_team)
for team in Dec_13_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Dec_13_WC_Standings.append(WC_team)

#December 20
December_20_url= 'https://www.basketball-reference.com/boxscores/?month=12&day=20&year=2022'
r9= requests.get(December_20_url)
soup= BeautifulSoup(r9.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Dec_20_EC= tables[0]
Dec_20_WC= tables[1]
Dec_20_EC_Standings=[]
Dec_20_WC_Standings= []
for team in Dec_20_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Dec_20_EC_Standings.append(EC_team)
for team in Dec_20_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Dec_20_WC_Standings.append(WC_team)

#December 27
December_27_url= 'https://www.basketball-reference.com/boxscores/?month=12&day=27&year=2022'
r10= requests.get(December_27_url)
soup= BeautifulSoup(r10.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Dec_27_EC= tables[0]
Dec_27_WC= tables[1]
Dec_27_EC_Standings=[]
Dec_27_WC_Standings= []
for team in Dec_27_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Dec_27_EC_Standings.append(EC_team)
for team in Dec_27_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Dec_27_WC_Standings.append(WC_team)

#January 3
January_3_url= 'https://www.basketball-reference.com/boxscores/?month=1&day=3&year=2023'
r11= requests.get(January_3_url)
soup= BeautifulSoup(r11.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Jan_3_EC= tables[0]
Jan_3_WC= tables[1]
Jan_3_EC_Standings=[]
Jan_3_WC_Standings= []
for team in Jan_3_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_3_EC_Standings.append(EC_team)
for team in Jan_3_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_3_WC_Standings.append(WC_team)

#January 10
January_10_url= 'https://www.basketball-reference.com/boxscores/?month=1&day=10&year=2023'
r12= requests.get(January_10_url)
soup= BeautifulSoup(r12.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Jan_10_EC= tables[0]
Jan_10_WC= tables[1]
Jan_10_EC_Standings=[]
Jan_10_WC_Standings= []
for team in Jan_10_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_10_EC_Standings.append(EC_team)
for team in Jan_10_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_10_WC_Standings.append(WC_team)

#January 17
January_17_url= 'https://www.basketball-reference.com/boxscores/?month=1&day=17&year=2023'
r13= requests.get(January_17_url)
soup= BeautifulSoup(r13.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Jan_17_EC= tables[0]
Jan_17_WC= tables[1]
Jan_17_EC_Standings=[]
Jan_17_WC_Standings= []
for team in Jan_17_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_17_EC_Standings.append(EC_team)
for team in Jan_17_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_17_WC_Standings.append(WC_team)

#January 24
January_24_url= 'https://www.basketball-reference.com/boxscores/?month=1&day=24&year=2023'
r14= requests.get(January_24_url)
soup= BeautifulSoup(r14.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Jan_24_EC= tables[0]
Jan_24_WC= tables[1]
Jan_24_EC_Standings=[]
Jan_24_WC_Standings= []
for team in Jan_24_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_24_EC_Standings.append(EC_team)
for team in Jan_24_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_24_WC_Standings.append(WC_team)

#January 31
January_31_url= 'https://www.basketball-reference.com/boxscores/?month=1&day=31&year=2023'
r15= requests.get(January_31_url)
soup= BeautifulSoup(r15.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Jan_31_EC= tables[0]
Jan_31_WC= tables[1]
Jan_31_EC_Standings=[]
Jan_31_WC_Standings= []
for team in Jan_31_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_31_EC_Standings.append(EC_team)
for team in Jan_31_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Jan_31_WC_Standings.append(WC_team)

#February 7
February_7_url= 'https://www.basketball-reference.com/boxscores/?month=2&day=7&year=2023'
r16= requests.get(February_7_url)
soup= BeautifulSoup(r16.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Feb_7_EC= tables[0]
Feb_7_WC= tables[1]
Feb_7_EC_Standings=[]
Feb_7_WC_Standings= []
for team in Feb_7_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Feb_7_EC_Standings.append(EC_team)
for team in Feb_7_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Feb_7_WC_Standings.append(WC_team)

#February 14
February_14_url= 'https://www.basketball-reference.com/boxscores/?month=2&day=14&year=2023'
r17= requests.get(February_14_url)
soup= BeautifulSoup(r17.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Feb_14_EC= tables[0]
Feb_14_WC= tables[1]
Feb_14_EC_Standings=[]
Feb_14_WC_Standings= []
for team in Feb_14_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Feb_14_EC_Standings.append(EC_team)
for team in Feb_14_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Feb_14_WC_Standings.append(WC_team)

#February 21
February_21_url= 'https://www.basketball-reference.com/boxscores/?month=2&day=21&year=2023'
r18= requests.get(February_21_url)
soup= BeautifulSoup(r18.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Feb_21_EC= tables[0]
Feb_21_WC= tables[1]
Feb_21_EC_Standings=[]
Feb_21_WC_Standings= []
for team in Feb_21_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Feb_21_EC_Standings.append(EC_team)
for team in Feb_21_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Feb_21_WC_Standings.append(WC_team)

#February 28

February_28_url= 'https://www.basketball-reference.com/boxscores/?month=2&day=28&year=2023'
r19= requests.get(February_28_url)
soup= BeautifulSoup(r19.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Feb_28_EC= tables[0]
Feb_28_WC= tables[1]
Feb_28_EC_Standings=[]
Feb_28_WC_Standings= []
for team in Feb_28_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Feb_28_EC_Standings.append(EC_team)
for team in Feb_28_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Feb_28_WC_Standings.append(WC_team)

#March 7

March_7_url= 'https://www.basketball-reference.com/boxscores/?month=3&day=7&year=2023'
r20= requests.get(March_7_url)
soup= BeautifulSoup(r20.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Mar_7_EC= tables[0]
Mar_7_WC= tables[1]
Mar_7_EC_Standings=[]
Mar_7_WC_Standings= []
for team in Mar_7_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Mar_7_EC_Standings.append(EC_team)
for team in Mar_7_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Mar_7_WC_Standings.append(WC_team)

#March 14
March_14_url= 'https://www.basketball-reference.com/boxscores/?month=3&day=14&year=2023'
r21= requests.get(March_14_url)
soup= BeautifulSoup(r21.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Mar_14_EC= tables[0]
Mar_14_WC= tables[1]
Mar_14_EC_Standings=[]
Mar_14_WC_Standings= []
for team in Mar_14_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Mar_14_EC_Standings.append(EC_team)
for team in Mar_14_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Mar_14_WC_Standings.append(WC_team)

#March 21
March_21_url= 'https://www.basketball-reference.com/boxscores/?month=3&day=21&year=2023'
r22= requests.get(March_21_url)
soup= BeautifulSoup(r22.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Mar_21_EC= tables[0]
Mar_21_WC= tables[1]
Mar_21_EC_Standings=[]
Mar_21_WC_Standings= []
for team in Mar_21_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Mar_21_EC_Standings.append(EC_team)
for team in Mar_21_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Mar_21_WC_Standings.append(WC_team)

#March 28
March_28_url= 'https://www.basketball-reference.com/boxscores/?month=3&day=28&year=2023'
r23= requests.get(March_28_url)
soup= BeautifulSoup(r23.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Mar_28_EC= tables[0]
Mar_28_WC= tables[1]
Mar_28_EC_Standings=[]
Mar_28_WC_Standings= []
for team in Mar_28_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Mar_28_EC_Standings.append(EC_team)
for team in Mar_28_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Mar_28_WC_Standings.append(WC_team)

#April 4
April_4_url= 'https://www.basketball-reference.com/boxscores/?month=4&day=4&year=2023'
r24= requests.get(April_4_url)
soup= BeautifulSoup(r24.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Apr_4_EC= tables[0]
Apr_4_WC= tables[1]
Apr_4_EC_Standings=[]
Apr_4_WC_Standings= []
for team in Apr_4_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Apr_4_EC_Standings.append(EC_team)
for team in Apr_4_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Apr_4_WC_Standings.append(WC_team)

#April 9
April_9_url= 'https://www.basketball-reference.com/boxscores/?month=4&day=9&year=2023'
r25= requests.get(April_9_url)
soup= BeautifulSoup(r25.text, 'html.parser')
tables= soup.find_all('table', class_= 'suppress_all sortable stats_table')
Apr_9_EC= tables[0]
Apr_9_WC= tables[1]
Apr_9_EC_Standings=[]
Apr_9_WC_Standings= []
for team in Apr_9_EC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    EC_team= row.find('th', class_='left').text.replace("*", "")
    Apr_9_EC_Standings.append(EC_team)
for team in Apr_9_WC.find_all('tbody'):
  rows= team.find_all('tr')
  for row in rows:
    WC_team= row.find('th', class_='left').text.replace("*", "")
    Apr_9_WC_Standings.append(WC_team)

#Output
EC_dict={
    1: Oct_25_EC_Standings,
    2: Nov_1_EC_Standings,
    3: Nov_8_EC_Standings,
    4: Nov_15_EC_Standings,
    5: Nov_22_EC_Standings,
    6: Nov_29_EC_Standings,
    7: Dec_6_EC_Standings,
    8: Dec_13_EC_Standings,
    9: Dec_20_EC_Standings,
    10:Dec_27_EC_Standings,
    11:Jan_3_EC_Standings,
    12:Jan_10_EC_Standings,
    13:Jan_17_EC_Standings,
    14:Jan_24_EC_Standings,
    15:Jan_31_EC_Standings,
    16:Feb_7_EC_Standings,
    17:Feb_14_EC_Standings,
    18:Feb_21_EC_Standings,
    19:Feb_28_EC_Standings,
    20:Mar_7_EC_Standings,
    21:Mar_14_EC_Standings,
    22:Mar_21_EC_Standings,
    23:Mar_28_EC_Standings,
    24:Apr_4_EC_Standings,
    25:Apr_9_EC_Standings,
}
WC_dict={
    1: Oct_25_WC_Standings,
    2: Nov_1_WC_Standings,
    3: Nov_8_WC_Standings,
    4: Nov_15_WC_Standings,
    5: Nov_22_WC_Standings,
    6: Nov_29_WC_Standings,
    7: Dec_6_WC_Standings,
    8: Dec_13_WC_Standings,
    9: Dec_20_WC_Standings,
    10:Dec_27_WC_Standings,
    11:Jan_3_WC_Standings,
    12:Jan_10_WC_Standings,
    13:Jan_17_WC_Standings,
    14:Jan_24_WC_Standings,
    15:Jan_31_WC_Standings,
    16:Feb_7_WC_Standings,
    17:Feb_14_WC_Standings,
    18:Feb_21_WC_Standings,
    19:Feb_28_WC_Standings,
    20:Mar_7_WC_Standings,
    21:Mar_14_WC_Standings,
    22:Mar_21_WC_Standings,
    23:Mar_28_WC_Standings,
    24:Apr_4_WC_Standings,
    25:Apr_9_WC_Standings,
}
date_dict={
    1: "October 25th, 2022",
    2: "November 1st, 2022",
    3: "November 8th, 2022",
    4: "November 15th, 2022",
    5: "November 22nd, 2022",
    6: "November 29th, 2022",
    7: "December 6th, 2022",
    8: "December 13th 2022",
    9: "December 20th, 2022",
    10:"December 27th, 2022",
    11:"January 3rd, 2023",
    12:"January 10th, 2023",
    13:"January 17th, 2023",
    14:"January 24th, 2023",
    15:"January 31st, 2023",
    16:"February 7th, 2023",
    17:"February 14th, 2023",
    18:"February 21st, 2023",
    19:"February 28th, 2023",
    20:"March 7th, 2023",
    21:"March 14th, 2023",
    22:"March 21st, 2023",
    23:"March 28th, 2023",
    24:"April 4th, 2023",
    25:"April 9th, 2023",
}
def Program():
  print("First, choose either the Eastern or Western Conference. Then, choose a team from that conference. Finally, enter a week from the regular season (1-25) to see where the team ranked at the end of that week during the 2022-2023 regular season!")
  print()
  conference=input("Eastern or Western Conference? (E=Eastern, W=Western)")
  print()
  team= input("Team? (e.g. Boston Celtics, Denver Nuggets, etc.)")
  print()
  week= int(input("Week?(1-25)"))
  print()
  if week<1 or week>25:
    print("ERROR: Please try again.")
  else:
    if conference=="E":
      if team in EC_dict[week]:
        print("On "+date_dict[week]+", at the end of week "+str(week)+" of the 2022-2023 regular season, the "+team+" were number "+ str(EC_dict[week].index(team)+1)+" in the Eastern Conference!")
        if week>1:
          difference= (EC_dict[week-1].index(team)+1)-(EC_dict[week].index(team)+1)
          if difference<0:
            print("The "+team+" fell "+str(abs(difference))+" position(s) from number "+str(EC_dict[week-1].index(team)+1)+" the previous week.")
          elif difference>0:
            print("The "+team+" rose "+str(abs(difference))+" position(s) from number "+str(EC_dict[week-1].index(team)+1)+" the previous week.")
          else:
            print("The "+team+" remained in the same position as the previous week.")

        print()
      else:
        print("ERROR: Please try again.")
    elif conference=="W":
      if team in WC_dict[week]:
        print("On "+date_dict[week]+", at the end of week "+str(week)+" of the 2022-2023 regular season, the "+team+" were number "+ str(WC_dict[week].index(team)+1)+" in the Western Conference!")
        if week>1:
          difference= (WC_dict[week-1].index(team)+1)-(WC_dict[week].index(team)+1)
          if difference<0:
            print("The "+team+" fell "+str(abs(difference))+" position(s) from number "+str(WC_dict[week-1].index(team)+1)+" the previous week.")
          elif difference>0:
            print("The "+team+" rose "+str(abs(difference))+" position(s) from number "+str(WC_dict[week-1].index(team)+1)+" the previous week.")
          else:
            print("The "+team+" remained in the same position as the previous week.")
        print()
      else:
        print("ERROR: Please try again.")
    else:
      print("ERROR: Please try again.")
while True:
  print("Welcome to the 2022-2023 NBA Regular Season Weekly Standings Archive! Please choose one of the two menu items (Type 1 or 2)")
  print("1. Continue")
  print("2. Quit")
  option=int(input())
  if option==1:
    Program()
  elif option==2:
    break
  else:
    print("ERROR: Please try again.")
