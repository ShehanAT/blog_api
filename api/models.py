from django.db import models
from jsonfield import JSONField 
# Create your models here

class Post(models.Model):
    author = models.CharField(max_length=100)
    author_id = models.IntegerField()
    likes = models.IntegerField(default=0)
    popularity = models.FloatField()
    reads = models.BigIntegerField()
    tags = JSONField(null=False)

