from django.db import models

# Create your models here.
class dbms(models.Model):
    questions=models.CharField(max_length=1000)
    marks=models.IntegerField(default=4)
    

