from django.urls import URLPattern, path


from .views.add_user import page_form
from .views.user_home import home_page
from .views.login_user import login_page
from .views.new_pass import change_form,forgot_form
from .views.logged_in import logged_page
from .views.emailp import email_page


urlpatterns=[
    path('home',home_page),
    path('createform',page_form),
    path('loginpage',login_page),
    path('changepassword',change_form),
    path('forgotpassword/<str:uniqueid>',forgot_form),
    path('loggedpage',logged_page),
    path('email',email_page),

]