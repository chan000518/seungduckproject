from django.shortcuts import render
from .backend import *
from .models import Luck
from datetime import date

# 유저와 연결된 luck인스턴스 생성(유저 회원 가입시)
def luck_create(user):
    luck_cnt = luck_by_gpt_api(user)
    luck = Luck.objects.create(
        user = user,
        names = luck_names_from(luck_cnt), 
        contents = luck_cnt, 
    )
    return luck

# 유저와 연결된 luck인스턴스 업데이트(트래픽이 적은 시간에 실행 || 갱신 요청시 처리)
def luck_update(luck):
    luck_cnt = luck_by_gpt_api(luck.user)
    luck.names = luck_names_from(luck_cnt)
    luck.contents = luck_cnt
    luck.save()
    return luck

# 유저와 연결된 luck인스턴스 detail view
def luck_detail(request):
    try:
        luck = Luck.objects.get(user=request.user)
    except Luck.DoesNotExist:
        luck = luck_create(request.user)
    except Luck.MultipleObjectsReturned:
        luck = Luck.objects.filter(user=request.user)[0]
        Luck.objects.filter(user=request.user)[1].delete()

    if luck.date == date.today():
        if luck.names == '':
            luck = luck_update(luck)
            ctx = {
            'luck' : luck,
            }    
        else:
            ctx = {
            'luck' : luck,
            }
    else:
        ctx = {
           'luck' : luck_update(luck),
        }    
    return render(request, 'Todays/luck_detail.html', ctx)