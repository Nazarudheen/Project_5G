from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    City = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)

class SignUpDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="Profile Image1",null=True,blank=True)

class CartDB(models.Model):
    UserName = models.CharField(max_length=100,null=True,blank=True)
    ProName =  models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    TotalPice = models.IntegerField(null=True,blank=True)
