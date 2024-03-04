from config.settings import WEATHER_API_KEY
import requests
import json
from datetime import date, datetime, timedelta
from .models import Weather
from .mapToGrid import mapToGrid
import math

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

    # basetime을 2000으로 하면 21시, 22시, 23시, 00시, 01시가 나옴
    response = requests.get(f'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={WEATHER_API_KEY}&pageNo=1&numOfRows=60&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}')
    data = response.json()
    weather_data = data['response']['body']['items']['item']
    
    # 필요한 카테고리
    # 기온 - "TMP"
    # 하늘상태: 맑음(1) 구름많은(3) 흐림(4) - "SKY"
    # 강수 형태 - 없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4) - "PTY"
    # 강수 확률 - "POP"
    categories = ["TMP", "SKY", "PTY", "POP"]       

    weather_dict = {}       # weather 딕셔너리 생성

    # 동일한 fcstTime을 기준으로 데이터를 반복하여 딕셔너리에 추가
    for data in weather_data:
        fcst_time = data["fcstTime"]
        category = data["category"]
        value = data["fcstValue"]
    
        # 선택한 카테고리에 해당하는 데이터만 딕셔너리에 추가
        if category in categories:
            if fcst_time not in weather_dict:
                weather_dict[fcst_time] = {}
            weather_dict[fcst_time][category] = value

    return weather_dict

def get_nx_ny():
    response = requests.get("http://www.geoplugin.net/json.gp")     # 현재 IP로 현 위치의 위도 경도를 얻을 수 있는 API 
    
    if (response.status_code != 200):
        print("현재 좌표를 불러올 수 없음")
    else:
        location = response.json()
        # mapToGrid 함수로 받아 온 위도, 경도를 nx, ny로 변환
        nx, ny = mapToGrid(float(location["geoplugin_latitude"]), float(location["geoplugin_longitude"]))

    return nx, ny