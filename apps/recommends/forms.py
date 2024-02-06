from django import forms
from .models import Recommend, RecommendPost

class RecommendForm(forms.ModelForm):
    class Meta:     
        model = Recommend
        fields = ['recommend_name']
        labels = {      # label 속성을 지정해 필드를 한글로 화면에 표시 가능
            'recommend_name': '추천 목록',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = RecommendPost
        fields = ['content']
        labels = {
            'content': '컨텐츠',
        }
