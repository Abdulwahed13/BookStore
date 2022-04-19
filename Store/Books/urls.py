from django.urls import URLPattern, path

# from Books.views.login_user import Login

from .views.add_book import AddBook 
from .views.update_book import UpdateBook 
from .views.delete_book import DeleteBook 
from .views.get_book import GetBook
from .views.list import ListBook 


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'file_url',GetBook)

urlpatterns = [
    path('create',AddBook.as_view()),
    path('update',UpdateBook.as_view()),
    path('getbook/<str:id>',GetBook.as_view()),
    path('deletebook/<str:id>',DeleteBook.as_view()),
    path('list',ListBook.as_view()),

]