from django.shortcuts import render
from ..models.user_details import UserDetails
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



def logged_page(request):
    return render(request,'logedin.html')