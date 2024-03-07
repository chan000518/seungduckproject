from django.shortcuts import render
from django.http import HttpResponse
from .models import Weather
from .backend import get_weather
from datetime import datetime

now = datetime.now()

def weather_create(request):
    # 날씨 정보는 총 5시간 분량의 정보를 출력하기 위해 count 5까지 반복문 진행하고 break
    count = 0       
    weather_data_list = get_weather()

    for time, weather_data in weather_data_list.items():
        if count == 5:
            break
        time_hour = int(time[:2])  # 시간을 정수로 변환
        if time_hour >= now.hour or time_hour < (now.hour - 18) % 24:  # 18시간 전의 시간까지 포함하여 출력
            forecast_time = f"{time[:2]}:{time[2:]}"        # 시간은 00:00 형태로 출력
            Weather.objects.create(
                user=request.user, 
                time=forecast_time,
                temperature=weather_data['TMP'],
                sky=weather_data["SKY"],
                rain=weather_data["PTY"],
                rain_p=weather_data["POP"]
            )
        count += 1

    return HttpResponse("Weather data created successfully")

def weather_update(request):
    weathers = Weather.objects.filter(user=request.user)
    weathers.delete()
    weather_create(request)
    return HttpResponse("Weather data updated successfully")

def weather_detail(request):        # 아직 미완입니다.
    if Weather.objects.exists():
        # 이미 모델이 생성되어 있는 경우, 기존 모델을 반환
        weather_update(request)    
    else:
        weather_create(request)
    weather_data = Weather.objects.order_by('time')
    ctx ={"weather_data": weather_data}

    return render(request, 'Todays/weather_detail.html', ctx)
