from django.shortcuts import render
from ..models.user_details import UserDetails
from django.shortcuts import render
from ..forms import EmailPage
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
def email_page(request):
    form=EmailPage(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            email = request.POST['email']
            if UserDetails.objects.filter(email=form.cleaned_data['email']).exists():
                newid=random.randint(100,999)
                UserDetails.objects.filter(email=form.cleaned_data['email']).update(uniqueid=newid)
                messages.success(request, f'A reset link has been sent to your provided email')
                send_mail(
                        'Resent link to change the password',
                        "http://127.0.0.1:8000/register/forgotpassword/"+str(newid),
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=['abdul@innomick.com'],
                        fail_silently=False,
                    )
            else:
                messages.warning(request, f'The email you entered does not exist')
    return render(request,'email.html', {'form':form, 'title':'log in'})