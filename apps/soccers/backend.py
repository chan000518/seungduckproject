import requests
from bs4 import BeautifulSoup as bs

# 웹 페이지에서 데이터를 가져오기.
date = '20240225' 
url = (f"https://sports.daum.net/prx/hermes/api/game/schedule.json?page=1&leagueCode=epl%2Cprimera%2Cbundesliga%2Cseriea%2Cligue1%2Ceredivisie%2Cuefacl%2Cuefacup%2Cepl_cup%2Cfacup%2Ccopadelrey&fromDate={date}&toDate={date}")
data = requests.get(url)

# 가져온 json데이터를 파이썬 json객체로
data = data.json()

# print(data) # 데이터 출력시 딕셔너리형태
#  딕셔너리 출력
# for key,val in data.items():
#     print(key)
#     print(val)

soccerSchedule = data['schedule'][date]

for game in soccerSchedule:
    #print(game)
    print(game['startTime'])
    print(game['homeTeamName'])
    print(game['awayTeamName'])