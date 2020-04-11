from django.db import models

# Create your models here.
class User(models.Model):
    fName=models.CharField(max_length=10,null=True)
    lName=models.CharField(max_length=10,null=True)
    Email=models.CharField(max_length=80,null=True)
    Password=models.CharField(max_length=20,null=True)

class Company(models.Model):
    C_Name=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=80,null=True)
    Password=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)


class Spec(models.Model):
    companyid= models.CharField(max_length=50,null=True)
    model = models.CharField(max_length=50,null=True)
    network= models.CharField(max_length=80,null=True)
    body = models.CharField(max_length=20,null=True)
    display = models.CharField(max_length=50,null=True)
    platform = models.CharField(max_length=80,null=True)
    memory= models.CharField(max_length=20,null=True)
    cpu=models.CharField(max_length=50,null=True)
    mainCam = models.CharField(max_length=50,null=True)
    selfieCam = models.CharField(max_length=80,null=True)
    phfeatures = models.CharField(max_length=20,null=True)
    battery = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=80,null=True)
    image= models.ImageField(upload_to='media/')

class comment(models.Model):
    specid=models.CharField(max_length=50,null=True)
    comments=models.CharField(max_length=50,null=True)
    username=models.CharField(max_length=50,null=True)
    caption=models.CharField(max_length=50,null=True)

class ajeesh(models.Model):
    name=models.CharField(max_length=10)
    lsname=models.CharField(max_length=10)