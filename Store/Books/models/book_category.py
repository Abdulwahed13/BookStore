import imp
from tkinter import CASCADE
from django.db import models
import uuid
from base.model import Base

class BookCategory(Base):
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default=True)

    class Meta:
        db_table = 'book_category'
        app_label = 'Books'
