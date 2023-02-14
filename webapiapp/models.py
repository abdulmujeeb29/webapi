from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class userProfile(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField()


class buisnessProfile(models.Model):
    company_owner = models.CharField(max_length=50)
    company_name =models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    email = models.EmailField()
    phone_num = PhoneNumberField()
    description = models.CharField(max_length=10000)