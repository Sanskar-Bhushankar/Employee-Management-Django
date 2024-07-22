from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    working=models.BooleanField(default=False)
    department=models.CharField(max_length=10)