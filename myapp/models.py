from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    email =  models.CharField(max_length=100)

    def __str__(self): 

        return f"{self.name}" 
