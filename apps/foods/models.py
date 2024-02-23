from django.db import models
from users.models import User
from datetime import date

# Create your models here.
class Food(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='food')
    date = models.DateField(auto_now=True)
    names = models.CharField(max_length = 50)
    contents = models.TextField()

    def __str__(self):
        return self.names
    def is_today(self):
        return self.date == date.today()

