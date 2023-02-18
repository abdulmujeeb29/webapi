from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class userProfile(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__(self) -> str:
        return self.name

Rating = (
    ('1', '1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),

)
class buisnessProfile(models.Model):
    business_name = models.CharField(max_length=50,blank=True)
    company_website=models.CharField(max_length=50,blank=True)
    address= models.CharField(max_length=100)
    state = models.CharField(max_length=50,blank=True)
    buisness_phone= PhoneNumberField()
    buisness_description = models.CharField(max_length=1000,blank=True)
    buisness_images = models.ImageField(null= True,blank=True,upload_to= "images/")
    other_details =models.CharField(max_length=1000,blank=True)

    def __str__(self) -> str:
        return self.business_name
    

# class review(models.Model):
#     user_rating =models.CharField(max_length=5, choices=Rating ,default=1)
#     review =models.CharField(max_length=50,blank=True)
#     review_images= models.ImageField(blank=True)