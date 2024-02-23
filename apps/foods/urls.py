from django.urls import path
from . import views

app_name = 'foods'

urlpatterns =[
    path('detail/', views.food_detail, name='detail')
]