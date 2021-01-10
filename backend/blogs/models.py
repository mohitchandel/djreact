from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime, date

class Blog(models.Model):    
    blogId  = models.AutoField(primary_key=True)
    title   = models.CharField(max_length=128, default=None ,blank = False ,null = False)
    images  = models.ImageField(blank=True ,null=True, upload_to="images/")
    description = RichTextField(blank = False ,null = False, default=None)
    author  = models.CharField(max_length=128, null = False, default='Mohit')
    createdAt = models.DateTimeField()
    categoryOne = models.CharField(max_length=128, blank = True, default=None, null=True, name="Category One")
    categoryTwo = models.CharField(max_length=128, blank = True, default=None, null=True, name="Category Two")
    categoryThree = models.CharField(max_length=128, blank = True, default=None, null=True, name="Category Three")

    def __str__(self):
        return self.title
