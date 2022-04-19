from tkinter import CASCADE
from trace import Trace
from xml.dom.minidom import Attr
from django.db import models
import uuid

from django.forms import EmailField
from django.contrib.auth.models import AbstractBaseUser, UserManager

class UserDetails(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100,error_messages={'required':'Enter your first name'})
    last_name=models.CharField(max_length=100,error_messages={'required':'Enter your last name'})
    email=models.EmailField(max_length=100,error_messages={'required':'Enter your email'})
    password=models.CharField(max_length=100,error_messages={'required':'Enter your password'})
    password2=models.CharField(max_length=100)
    is_delete=models.CharField(max_length=100,default=False)
    status=models.CharField(max_length=100,default=True)
    uniqueid=models.CharField(max_length=100,blank=True)

    class Meta:
        db_table='user_details'
        app_label='Books'