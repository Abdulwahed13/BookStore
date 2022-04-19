from django import forms
# from .

# class BooksForm(forms.ModelForm):
#     class Meta:
#         model=Book

#         fields=[
#             'name',
#         ]

from .models.user_details import UserDetails
 
class RegForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = [
            'username','first_name', 'last_name', 
            'email', 'password','password2' 
        ]
        
class LoginPage(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields=[
            'email','password'
        ]


class EmailPage(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields=[
            'email',
        ]


class Changepage(forms.ModelForm):
    new_Password = forms.CharField(max_length=100)
    repass=forms.CharField(max_length=100)
    class Meta:
        model = UserDetails
        fields=[
            'password',
        ]


class Forgotpage(forms.ModelForm):
    new_Password = forms.CharField(max_length=100)
    repass=forms.CharField(max_length=100)
    class Meta:
        model = UserDetails
        fields=[

        ]
