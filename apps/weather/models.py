from django.db import models
from users.models import User
#from datetime import datetime

# Create your models here.    
class Location(models.Model):
    #id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=80, null=True, blank=True)
    longitude = models.FloatField(blank=True, null=True) #경도
    latitude  = models.FloatField(blank=True, null=True) #위도
    #description = models.CharField(max_length=100, blank=True, null=True)
  
    def __str__(self):
        return str(self.location_name)
    
class Weather(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='weather')
    current_time = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    temp = models.IntegerField(blank=True, null=True) #온도
    #humidity = models.IntegerField(blank=True, null=True) #습도
    rainfall = models.CharField(max_length=20, blank=True, null=True) #한시간 동안 강수량
    sky = models.IntegerField(blank=True, null=True) # 하늘 상태

    def __str__(self):
        return self.address + "-" + str(self.current_time)