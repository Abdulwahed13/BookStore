from tkinter import CASCADE
from django.db import models
import uuid

# Create your models here.
class Base(models.Model):
    id              =   models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_date    =   models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date    =   models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class BookCategory(Base):
    name=models.CharField(max_length=100)

    class Meta:
        db_table = 'book_category'
        app_label = 'Books'

class Book(Base):
    category=models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    class Meta:
        db_table = 'book'
        app_label = 'Books'
