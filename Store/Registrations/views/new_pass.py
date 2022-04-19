from django.shortcuts import redirect, render
from ..forms import Changepage,Forgotpage
from ..models.user_details import UserDetails
from django.contrib import messages
from django.contrib.auth.models import User


template="registration_form.html"
def change_form(request):
    form=Changepage(request.POST or None)
    if form.is_valid():
        password = request.POST["password"]
        new_password = request.POST["new_Password"]
        repass=request.POST["repass"]
        if UserDetails.objects.filter(password=form.cleaned_data['password']).exists():
            if new_password==repass:
                UserDetails.objects.filter(password=password).update(password=form.cleaned_data['new_Password'])
                messages.success(request,f'Password Has been updated')
                return render(request,'changepass.html', {'form':form, 'title':'log in'})
            else:
                messages.warning(request, f'passwords do not match')
                return render(request,'changepass.html', {'form':form, 'title':'log in'})

        else:
            messages.warning(request, f'password you entered is incorrect')
            return render(request,'changepass.html', {'form':form, 'title':'log in'})
    else:
        return render(request,'changepass.html', {'form':form, 'title':'log in'})


def forgot_form(request,uniqueid):
    form=Forgotpage(request.POST or None)
    if form.is_valid():
        new_password = request.POST["new_Password"]
        repass=request.POST["repass"]
        if new_password == repass:
            UserDetails.objects.filter(uniqueid=uniqueid).update(password=form.cleaned_data['new_Password'])
            messages.success(request,f'Password Has been updated')
            return render(request,'forgotpass.html', {'form':form, 'title':'log in'})
        else:
            messages.warning(request, f'passwords do not match')
            return render(request,'changepass.html', {'form':form, 'title':'log in'})
    return render(request,'forgotpass.html', {'form':form, 'title':'log in'})