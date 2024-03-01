from django.db import models
from users.models import User

# Create your models here.    
class Weather(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='weather')
    current_time = models.DateTimeField(auto_now=True)
    #address = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    temp = models.IntegerField(blank=True, null=True) #온도
    rain = models.CharField(max_length=20, blank=True, null=True) #강수 상태
    rain_p = models.IntegerField(blank=True, null=True) #강수 확률
    sky = models.CharField(blank=True, null=True) # 하늘 상태
    