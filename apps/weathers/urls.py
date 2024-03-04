from django.urls import path
from . import views

app_name = 'weathers'

urlpatterns =[
    path('detail/', views.weather_detail, name='detail')
]