from django.db import models
from datetime import date

# Create your models here.
class Soccer(models.Model):
    #user 필요시 아래 코드 사용
    #user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='soccer')
    league = models.CharField(max_length = 50)
    hometeam = models.CharField(max_length = 50)
    awayteam = models.CharField(max_length = 50)
    time = models.CharField(max_length = 50)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.league
    def __str__(self):
        return self.hometeam
    def __str__(self):
        return self.awayteam
    def __str__(self):
        return self.time
    def __str__(self):
        return self.date == date.today()
