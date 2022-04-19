from tkinter import CASCADE
from django.db import models
import uuid
from base.model import Base
from ..models.book_category import BookCategory 

class Book(Base):
    category=models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    is_delete=models.CharField(max_length=100,default=False)
    status=models.CharField(max_length=100,default=True)
    file_url=models.FileField(upload_to='documents',max_length=200,blank=True)

    class Meta:
        db_table = 'book'
        app_label = 'Books'