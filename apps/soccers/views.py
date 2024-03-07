from django.shortcuts import render
from .backend import get_soccer_schedule
from .models import Soccer
from datetime import date

def soccer_create():
    soccerSchedule = get_soccer_schedule()
    for game in soccerSchedule:
        # 유럽 4대리그만 고려하여 soccer 객체 생성
        if game['leagueName'] in ('라리가', '세리에A', '분데스리가', '프리미어리그'):
            soccer = Soccer.objects.create(
                league=game['leagueName'],
                time=game['startTime'], 
                hometeam=game['homeTeamName'],
                awayteam=game['awayTeamName'],
            )

    return Soccer.objects.order_by('league')
    
def soccer_update(soccer):
   # if Soccer.date == date.today()
    soccerSchedule = get_soccer_schedule()
    for game in soccerSchedule:
        # 유럽 4대리그만 고려하여 soccer 객체 생성
        if game['leagueName'] in ('라리가', '세리에A', '분데스리가', '프리미어리그'):
                soccer.league=game['leagueName'],
                soccer.time=game['startTime'], 
                soccer.hometeam=game['homeTeamName'],
                soccer.awayteam=game['awayTeamName'],
                soccer.date = date.today()
    
    return soccer




def soccer_detail(request):
    try:
        schedule_list = Soccer.objects.get()
    except Soccer.DoesNotExist:
        schedule_list = soccer_create()
    
    if Soccer.date == date.today():
        ctx = {
            'schedule_list' : schedule_list
        }
    else:
        schedule_list = soccer_update(schedule_list)
        schedule_list = Soccer.objects.order_by('league')
        ctx = {
            'schedule_list' : schedule_list
        }
    

    return render(request, 'Todays/soccer_detail.html', ctx)