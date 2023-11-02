from django.db import models
# from .forms import VechForm

# Create your models here.
class Vech(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=15)