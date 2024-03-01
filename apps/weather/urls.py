from django.urls import path
from . import views

app_name = 'weather'

urlpatterns =[
    path('detail/', views.weather_detail, name='detail')
]