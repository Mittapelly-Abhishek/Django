from django.db import models

# Create your models here.


class Employees (models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,blank=True,null=True)
    department=models.CharField(max_length=100,blank=True,null=True)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    date_joined=models.DateField(auto_now_add=True)


