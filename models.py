from django.db import models
from django.db import models
class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=255,unique=True)
    mno=models.IntegerField()
    password=models.CharField(max_length=20)

# Create your models here.
