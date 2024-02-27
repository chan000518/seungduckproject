from django.urls import path
from . import views

app_name = 'soccers'

urlpatterns =[
    path('detail/', views.soccer_detail, name='detail')
]