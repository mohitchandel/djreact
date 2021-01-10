from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime, date

class Blog(models.Model):    
    blogId  = models.AutoField(primary_key=True)
    title   = models.CharField(max_length=128, default=None ,blank = False)
    images  = models.ImageField(blank=True ,null=True, upload_to="images/")
    description = RichTextField(blank = False, default=None)
    author  = models.CharField(max_length=128, default='Mohit')
    createdAt = models.DateTimeField()
    categoryOne = models.CharField(max_length=128, blank = True, default=None, name="Category One")
    categoryTwo = models.CharField(max_length=128, blank = True, default=None, name="Category Two")
    categoryThree = models.CharField(max_length=128, blank = True, default=None, name="Category Three")

    def __str__(self):
        return self.title
