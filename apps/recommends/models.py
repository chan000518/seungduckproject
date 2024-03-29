from django.db import models
from django.contrib.auth.models import User   # 로그인 유저들(생일이 기록됨 -> 운세 등에 쓰일 정보)

class Recommend(models.Model):
    recommend_name = models.CharField(max_length = 10)
    def __str__(self):
        return self.recommend_name

class RecommendPost(models.Model):
    recommend_kind = models.ForeignKey(Recommend, on_delete = models.CASCADE, related_name='recommend')  # related_name : 역참조에 쓰임
    content = models.TextField()
    # user 
    # date

class music(models.Model):
    music = models.ForeignKey(RecommendPost, on_delete = models.CASCADE, related_name = 'music')
