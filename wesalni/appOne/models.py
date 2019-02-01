from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    def __str__(self):
        return self.username
    