from django.db import models
from admins.models import Products


# Create your models here.


class Register(models.Model):
    cname=models.CharField(max_length=50)
    cemail= models.CharField(max_length=50)
    cpaw = models.CharField(max_length=50)
    cmno= models.CharField(max_length=50)
    cadd = models.CharField(max_length=50)
    cpin = models.CharField(max_length=50)

class Purchase(models.Model):
    pname=models.CharField(max_length=50)
    pcat=models.CharField(max_length=50)
    pcost= models.CharField(max_length=50)
    pquality = models.CharField(max_length=50)
    pdec= models.CharField(max_length=50)
    cid=models.ForeignKey(Register,on_delete=models.CASCADE)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE)


class Msg(models.Model):
    msg=models.TextField()


