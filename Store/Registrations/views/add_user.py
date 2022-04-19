from django.shortcuts import render
from ..forms import RegForm
from ..models.user_details import UserDetails
from django.contrib import messages
from django.contrib.auth.models import User


template="registration_form.html"
def page_form(request):
    form=RegForm(request.POST or None)
    if form.is_valid():
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if UserDetails.objects.filter(email=form.cleaned_data['email']).exists():
            messages.info(request, f'email already exists please enter a different email')
            return render(request,template,{"form":form})
        elif password!=password2:
            messages.info(request, f'Passwords do not match')
            return render(request,template,{"form":form})
        else:
            form.save()
            messages.info(request, f'Registration was succesfull')
            return render(request,template,{"form":form})

    else:
        form=RegForm()
    return render(request,template,{"form":form})

