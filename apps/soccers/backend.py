import requests
from bs4 import BeautifulSoup as bs
from datetime import date
from .models import Soccer

date = date.today().strftime('%Y%m%d')          # 날짜 형식에 '-'는 없어야 하므로

def get_soccer_schedule():
    
    # 모델 없으면 모델 생성
    # 웹 페이지에서 데이터를 가져옵니다.
    url = (f"https://sports.daum.net/prx/hermes/api/game/schedule.json?page=1&leagueCode=epl%2Cprimera%2Cbundesliga%2Cseriea%2Cligue1%2Ceredivisie%2Cuefacl%2Cuefacup%2Cepl_cup%2Cfacup%2Ccopadelrey&fromDate={date}&toDate={date}")
    js = requests.get(url)
        
    # 가져온 json데이터를 파이썬 json객체로
    data = js.json()

    soccerSchedule = data['schedule'][date]     # schedule은 딕셔너리 이름, date는 키 값

    return soccerSchedule

