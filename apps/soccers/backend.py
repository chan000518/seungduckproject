import requests
from bs4 import BeautifulSoup as bs
from datetime import date
from .models import Soccer


date = date.today().strftime('%Y%m%d')          # 날짜 형식에 '-'는 없어야 하므로

def create_soccer_schedule():
    if Soccer.objects.exists():
        # 이미 모델이 생성되어 있는 경우, 기존 모델을 반환
        return Soccer.objects.order_by('league')        # 리그 순으로 정렬
    else:
        # 모델 없으면 모델 생성
        # 웹 페이지에서 데이터를 가져옵니다.
        url = (f"https://sports.daum.net/prx/hermes/api/game/schedule.json?page=1&leagueCode=epl%2Cprimera%2Cbundesliga%2Cseriea%2Cligue1%2Ceredivisie%2Cuefacl%2Cuefacup%2Cepl_cup%2Cfacup%2Ccopadelrey&fromDate={date}&toDate={date}")
        js = requests.get(url)
        
        # 가져온 json데이터를 파이썬 json객체로
        data = js.json()

        soccerSchedule = data['schedule'][date]     # schedule은 딕셔너리 이름, date는 키 값

        for game in soccerSchedule:
            # 유럽 4대리그만 고려하여 soccer 객체 생성
            if game['leagueName'] in ('라리가', '세리에A', '분데스리가', '프리미어리그'):
                soccer_obj = Soccer.objects.create(
                    league=game['leagueName'],
                    time=game['startTime'], 
                    hometeam=game['homeTeamName'],
                    awayteam=game['awayTeamName'],
                )

        return Soccer.objects.order_by('league')