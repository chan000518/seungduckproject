from django.db import models


# Create your models here.
class Recommend(models.Model):
    recommend_name = models.CharField()

class RecommendPost(models.model):
    recommend_kind = models.ForeignKey(Recommend, on_delete = models.CASCADE, related_name='recommend')
    content = models.TextField()
    # user 
    # date
    