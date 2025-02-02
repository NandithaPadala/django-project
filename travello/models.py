from django.db import models

# Create your models here.

class Destination(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 20)
    img = models.ImageField(upload_to='img',width_field=None,height_field=None,max_length=100)
    desc = models.CharField(max_length = 20)
    price =  models.IntegerField(default=0)
    offer = models.BooleanField(default=False)