from django.urls import path
from . import views

urlpatterns =[
    path('<int:recommend_id>/', views.detail, name='detail')
]