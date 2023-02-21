from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# from email_validator import validate_email
from validate_email import validate_email
from django.contrib.auth.models import User

# Create your models here.
class userProfile(models.Model):
    name =models.CharField(max_length=50,blank=False )
    email=models.EmailField(blank=False)
    
    def __str__(self) -> str:
        return self.name

Rating = (
    ('1', '1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),

)


alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]*$', 'Only alphanumeric characters are allowed.')
valid_phonenumber_format = RegexValidator(r'^+[0-9]$', 'enter a valid phone number format')
valid_url = RegexValidator(r'^(https:\/\/www\.|http:\/\/www\.|www\.)[a-zA-Z0-9]+\.[a-zA-Z]{2,5}$', 'enter a valid url')

def length_name(value ):
    if len(value) > 8 :
        raise ValidationError("name shouldn't  be more than 8 characters")
    
    
def address_length(value):
    if len(value) > 50:
        raise ValidationError("Address shouldn't be more than 50 characters")
    

def phone_number (value):
    if len(value)> 14:
        raise ValidationError('enter appropriate length of phone number ')
    



class buisnessProfile(models.Model):
    business_name = models.CharField(max_length=50,blank=True,null=True, validators=[alphanumeric, length_name])
    company_website=models.CharField(max_length=50,blank=True,null=True ,validators=[valid_url])
    address= models.CharField(max_length=100, validators=[address_length])
    state = models.CharField(max_length=50,blank=True)
    buisness_phone= PhoneNumberField(validators=[phone_number])
    email =models.EmailField(null=True)
    #buisness_phone= models.IntegerField(validators=[valid_phonenumber_format],blank=True,null=True)
    buisness_description = models.CharField(max_length=1000,blank=True)
    buisness_images = models.FileField(upload_to ='files',blank=True,null=True)
    other_details =models.CharField(max_length=250,blank=True)
    
    def __str__(self) -> str:
        return self.business_name
    

# class review(models.Model):
#     user_rating =models.CharField(max_length=5, choices=Rating ,default=1)
#     review =models.CharField(max_length=50,blank=True)
#     review_images= models.ImageField(blank=True)