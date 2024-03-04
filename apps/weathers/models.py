from django.db import models
from users.models import User

# Create your models here.    
class Weather(models.Model):
    #user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='weather')
    time = models.IntegerField(default='0') # 예보 시간
    temperature = models.IntegerField(default='0') #온도
    rain = models.IntegerField(default='0') #강수 상태
    rain_p = models.IntegerField(default='0') #강수 확률
    sky = models.IntegerField(default='0') # 하늘 상태
    