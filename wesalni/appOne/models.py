from django.db import models
#from phone_field import PhoneNumber
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    #date_of_birth= models.DateField(auto_now=False)
    #phone_number = PhoneNumber()
    def __str__(self):
        return self.username
        