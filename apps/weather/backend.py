from config.settings import WEATHER_API_KEY
import requests
import json
from datetime import date, datetime, timedelta
from .models import Weather
from .mapToGrid import mapToGrid

# 단기예보 정보를 조회하기 위해 발표일자, 발표시각, 예보지점 X좌표, 예보지점 Y 좌표의 조회 조건으로 발표일자, 발표시각, 자료구분문자, 예보 값, 예보일자, 예보시각, 예보지점 X 좌표, 예보지점 Y 좌표의 정보를 조회하는 기능
# nx : 예보지점의 x좌표값, ny : 예보지점의 y좌표값
def get_weather():

    nx, ny = get_nx_ny()
    now = datetime.now()
    today = date.today().strftime("%Y%m%d")
    yesterday = (now - timedelta(days=1)).strftime("%Y%m%d")

    if now.hour < 2 or (now.hour == 2 and now.minute < 10):
        base_time = "2300"
        base_date = yesterday
    elif now.hour < 5 or (now.hour == 5 and now.minute < 10):
        base_time = "0200"
        base_date = today
    elif now.hour < 8 or (now.hour == 8 and now.minute < 10):
        base_time = "0500"
        base_date = today
    elif now.hour < 11 or (now.hour == 11 and now.minute < 10):
        base_time = "0800"
        base_date = today
    elif now.hour < 14 or (now.hour == 14 and now.minute < 10):
        base_time = "1100"
        base_date = today
    elif now.hour < 17 or (now.hour == 17 and now.minute < 10):
        base_time = "1400"
        base_date = today
    elif now.hour < 20 or (now.hour == 20 and now.minute < 10):
        base_time = "1700"
        base_date = today
    elif now.hour < 23 or (now.hour == 23 and now.minute < 10):
        base_time = "2000"
        base_date = today
    else:
        base_time = "2300"
        base_date = today

    response = requests.get(f'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={WEATHER_API_KEY}&pageNo=1&numOfRows=60&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}')
    data = response.json()
    weather_data = data['body']['items']['item']

    # basetime을 2000으로 하면 21시, 22시, 23시, 00시, 01시가 나옴
    for item in weather_data:
        if item['category'] == 'TMP':        # 기온
            Weather.temp = item['fcstValue']
        # 하늘상태: 맑음(1) 구름많은(3) 흐림(4)
        if item['category'] == 'SKY':
            if item['fcstValue'] == 1:
                Weather.sky = "맑음"
            elif item['fcstValue'] == 3:
                Weather.sky = "구름많음"
            else:
                Weather.sky = "흐림"
        # 강수 형태 - 없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4) 
        if item['category'] == 'PTY':
            if item['fcstValue'] == 0:
                Weather.rain == "강수 없음"
            elif item['fcstValue'] == 1:
                Weather.rain == "비"
            elif item['fcstValue'] == 2:
                Weather.rain == "비/눈"
            elif item['fcstValue'] == 3:
                Weather.rain == "눈"
            else:
                Weather.rain == "소나기"
        # 강수 확률
        if item['category'] == 'POP':
            Weather.rain_p == item['fcstValue']

def get_nx_ny():
    response = requests.get("http://www.geoplugin.net/json.gp")     # 현재 IP로 현 위치의 위도 경도를 얻을 수 있는 API 

    if (response.status_code != 200):
        print("현재 좌표를 불러올 수 없음")
    else:
        location = json.loads(response.text)
        # mapToGrid 함수로 받아 온 위도, 경도를 nx, ny로 변환
        nx, ny = mapToGrid(location["geoplugin_latitude"], location["geoplugin_longitude"])

    return nx, ny