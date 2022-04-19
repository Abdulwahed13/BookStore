from django.shortcuts import render
from ..forms import RegForm
from ..models.user_details import UserDetails
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from ..forms import LoginPage
from django.contrib.auth.models import User




def login_page(request):
    form=LoginPage(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            # AuthenticationForm_can_also_be_used__
            email = request.POST['email']
            password = request.POST['password']
            # user = authenticate(request, username = email, password = password)
            if UserDetails.objects.filter(email=form.cleaned_data['email']).exists():
                if UserDetails.objects.filter(email=email).values('password')==form.cleaned_data['password']:
                    messages.success(request, f'Welcome')
                    return redirect("/logedin.html")
                else:
                    messages.warning(request, f'email and password do not match')
            else:
                messages.warning(request, f'account does not exit please enter correct details')
        # form = AuthenticationForm()
    return render(request,'login.html', {'form':form, 'title':'log in'})