from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=250, default=None ,blank = False ,null = False)

    def __str__(self):
        return self.name

class Blog(models.Model):    
    blogId  = models.AutoField(primary_key=True)
    title   = models.CharField(max_length=128, default=None ,blank = False ,null = False)
    images  = models.ImageField(blank=True ,null=True, upload_to="images/")
    discription = RichTextField(blank = True ,null = True)
    author  = models.CharField(max_length=128)
    createdAt = models.DateTimeField()
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True)
    category = models.ManyToManyField(Category)


    def __str__(self):
        return self.title
