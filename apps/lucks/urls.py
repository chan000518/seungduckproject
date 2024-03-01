from django.urls import path
from . import views

app_name = 'lucks'

urlpatterns =[
    path('detail/', views.luck_detail, name='detail')
]