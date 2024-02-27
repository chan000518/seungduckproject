from django.shortcuts import render
from .backend import create_soccer_schedule
from .models import Soccer

schedule_list = create_soccer_schedule()        # Soccer 모델 생성

def soccer_detail(request):
    ctx = {
        'schedule_list' : schedule_list
    }
    return render(request, 'soccers/soccer_detail.html', ctx)