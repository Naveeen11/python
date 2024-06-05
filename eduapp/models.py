from django.db import models

# Create your models here.
class student(models.Model):
    
    name = models.CharField(max_length=40)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    