from django.db import models

# Create your models here.

class UserReg(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,default="user@gmail.com")
    mobile=models.CharField(max_length=10)
    image=models.FileField(upload_to='profile/')
