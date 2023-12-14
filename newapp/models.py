from django.db import models
from rest_framework import serializers



# Create your models here.


class news(models.Model):
    taskname=models.CharField(max_length=50)
    user=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    date=models.DateField(auto_now_add=True)



class hotels(models.Model):
    movnm=models.CharField(max_length=50)
    rldt=models.DateField()
    chart=models.CharField(max_length=50)
    thnm=models.CharField(max_length=50)
    dirnm=models.CharField(max_length=50)
    rat=models.FloatField()



class productmodel(models.Model):
    productname=models.CharField(max_length=50)
    productimg=models.FileField()
    productdis=models.CharField(max_length=50)


class viewmodel(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.FloatField()



class newywmodel(models.Model):
    flightname=models.CharField(max_length=50)
    flightplace=models.CharField(max_length=50)
    flightpicture=models.FileField()
    flightdeparture=models.DateField()




class personmodel(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.FloatField()





class todosmodel(models.Model):
    emplyeename=models.CharField(max_length=50)
    emplyeelocation=models.CharField(max_length=50)
    employeeprofile=models.FileField()
    employdob=models.DateField()





































































