from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from accounts.managers import UserManager
from django.contrib.postgres.fields import ArrayField


RECRUITER_CHOICES = (
 ('vendor', 'Vendor'),
 ('employer', 'Employer')
)






# models.py 
class User(AbstractBaseUser):
    username = None
    first_name = models.CharField(max_length=12)
    middle_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    image1 = models.FileField(upload_to='documents/')
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    recruiter =models.CharField(max_length=50, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    job_title = models.CharField(max_length=40, default="")
    experience1 = models.IntegerField(default=0, blank=True)
    dob_city = models.CharField(max_length=40, default="")
    dob_state = models.CharField(max_length=40, default="")
    dob_country = models.CharField(max_length=40, default="")
    dob = models.CharField(max_length=40, default="")
    address = models.CharField(max_length=40, default="")
    location1 = models.CharField(max_length=40, default="")
    state = models.CharField(max_length=40, default="")
    country = models.CharField(max_length=40, default="")
    pin = models.CharField(max_length=40, default="")
    tel = models.CharField(max_length=40, default="")
    mob = models.CharField(max_length=40, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()




    


 
class Hotel(models.Model): 
    name = models.CharField(max_length=50) 
    hotel_Main_Img = models.ImageField(upload_to='images/') 


