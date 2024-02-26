from django.shortcuts import render
from .backend import food_by_gpt_api, food_names_from
from .models import Food
from datetime import date

# 유저와 연결된 food인스턴스 생성(유저 회원 가입시)
def food_create(user):
    food_cnt = food_by_gpt_api(user)
    food = Food.objects.create(
        user = user,
        names = food_names_from(food_cnt), 
        contents = food_cnt, 
    )
    return food

# 유저와 연결된 food인스턴스 업데이트(트래픽이 적은 시간에 실행 || 갱신 요청시 처리)
def food_update(food):
    food_cnt = food_by_gpt_api(food.user)
    food.names = food_names_from(food_cnt)
    food.contents = food_cnt
    food.save()
    return food

# 유저와 연결된 food인스턴스 detail view
def food_detail(request):
    try:
        food = Food.objects.get(user=request.user)
    except Food.DoesNotExist:
        food = food_create(request.user)

    if food.date == date.today():
        if food.names == '':
            ctx = {
            'food' : food_update(food),
            }    
        else:
            ctx = {
            'food' : food,
            }
    else:
        ctx = {
           'food' : food_update(food),
        }    
    return render(request, 'Todays/food_detail.html', ctx)