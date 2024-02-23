from django.shortcuts import render, get_object_or_404       # get_object_or_404 : 페이지가 존재하지 않음 출력
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import RecommendForm, PostForm

def scrapping_pottun():
    #스크래핑
    return g
# Create your views here.
def home(request):
    recommend_list = Recommend.objects.all()
    context = {'recommend_list': recommend_list}
    return render(request, 'Todays/recommend_list.html', context)

def detail(request, recommend_id):
    recommend_p = get_object_or_404(RecommendPost, pk=recommend_id)
    if recommend_p.kind == "운세":
        recommend_p.content = scrapping_pottun()
        recommend_p.save()
    elif
    elf
    context = {'recommend': recommend}
    return render(request, 'Todays/recommend_detail.html', context)

