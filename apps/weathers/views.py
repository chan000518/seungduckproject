from django.shortcuts import render
from .models import Weather
from .backend import get_weather
#from datetime import date

def weather_create():
    weather_data_list = get_weather()

    for time, weather_data in weather_data_list.items():
        weather = Weather.objects.create(
            #user=Weather.user,  # 사용자를 여기에 지정해야 합니다.
            time=time,
            temperature=weather_data['TMP'],
            sky=weather_data["SKY"],
            rain=weather_data["PTY"],
            rain_p=weather_data["POP"]
        )

    return weather


#def weather_create():
#    weather_data_list = {}
#    weather_data_list = get_weather()

#    for weather_data in weather_data_list:
#        weather = Weather.objects.create(
#            user = Weather.user,
#            time=weather_data['fcstTime'],
#            temperature=weather_data['TMP'],
#            sky=weather_data["sky"],
#            rain=weather_data["PTY"],
#            rain_p=weather_data["POP"]
#        )

#    return weather

def weather_detail(request):        # 아직 미완입니다.
    if Weather.objects.exists():
        # 이미 모델이 생성되어 있는 경우, 기존 모델을 반환
        weather = Weather.objects.get(user=request.user)     
    else:
        weather = weather_create()
    
    ctx ={"weather": weather}

    return render(request, 'Todays/weather_detail.html', ctx)
