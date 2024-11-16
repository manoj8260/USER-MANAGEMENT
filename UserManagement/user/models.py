from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=50)
    whatsapp_no = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255)
    registration_no = models.CharField(max_length=255)
    vat_no = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
          return self.username.username + '   '+self.role



   
    
    