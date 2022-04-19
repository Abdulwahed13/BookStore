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