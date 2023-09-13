from django.db import models

# Create your models here.
class Reviews(models.Model):
    user_hash = models.CharField(max_length= 100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    score = models.FloatField(null =True, blank= True)