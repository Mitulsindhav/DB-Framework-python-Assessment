from django.db import models
from superuser.models import client


# Create your models here.


class instruction1(models.Model):
    inst = models.TextField()
    client = models.ForeignKey(client, on_delete=models.CASCADE)

class document(models.Model):
    name=models.CharField(max_length=20)

class forgotpas(models.Model):
    email=models.EmailField()
