from config.settings import WEATHER_API_KEY
import requests
import json
from datetime import date, datetime, timedelta
#from .models import Weather

#단기예보 정보를 조회하기 위해 발표일자, 발표시각, 예보지점 X좌표, 예보지점 Y 좌표의 조회 조건으로 발표일자, 발표시각, 자료구분문자, 예보 값, 예보일자, 예보시각, 예보지점 X 좌표, 예보지점 Y 좌표의 정보를 조회하는 기능
# nx : 예보지점의 x좌표값, ny : 예보지점의 y좌표값
def check_weather(nx, ny):

    now = datetime.now()
    today = datetime.today().strftime("%Y%m%d")
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

    response = requests.get(f'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={WEATHER_API_KEY}&numOfRows=60&pageNo=1&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}&dataType=json')
    items = response.json()#.get('response').get('body').get('items')
    #print(items)
    data = dict()
    data['date'] = base_date

    weather_data = dict()

    for item in items['item']:
        # 기온
        if item['category'] == 'T1H':
            weather_data['tmp'] = item['fcstValue']
        # 습도
        if item['category'] == 'REH':
            weather_data['hum'] = item['fcstValue']
        # 하늘상태: 맑음(1) 구름많은(3) 흐림(4)
        if item['category'] == 'SKY':
            weather_data['sky'] = item['fcstValue']
        # 1시간 동안 강수량
        if item['category'] == 'RN1':
            weather_data['rain'] = item['fcstValue']

    print("response: ", weather_data)
    #print(weather_data['tmp'])
    return weather_data