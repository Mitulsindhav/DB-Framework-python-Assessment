from django.db import models
from superuser.models import client
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus



# Create your models here.

class Review1(models.Model):
    clientid = models.ForeignKey(client, on_delete=models.CASCADE)
    profession = models.CharField(max_length=30)
    msg = models.CharField(max_length=250)

class forgotpas1(models.Model):
    email=models.EmailField()



class Document(models.Model):
    client=models.ForeignKey(client, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/')



