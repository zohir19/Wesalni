from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_of_birth= models.DateField(auto_now=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    city =models.CharField(max_length=50)
    def __str__(self):
        return self.username
