from django.shortcuts import render
from .backend import create_soccer_schedule
from .models import *

def soccer_detail(request):
    schedule_list = create_soccer_schedule()        # Soccer 모델 생성
    ctx = {
        'schedule_list' : schedule_list
    }
    return render(request, 'Todays/soccer_detail.html', ctx)