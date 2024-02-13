from django.shortcuts import render, get_object_or_404       # get_object_or_404 : 페이지가 존재하지 않음 출력
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Recommend
from .forms import RecommendForm, PostForm

# Create your views here.
def home(request):
    recommend_list = Recommend.objects.all()
    context = {'recommend_list': recommend_list}
    return render(request, 'Todays/recommend_list.html', context)

def detail(request, recommend_id):
    recommend = get_object_or_404(Recommend, pk=recommend_id)
    context = {'recommend': recommend}
    return render(request, 'Todays/recommend_detail.html', context)
    
