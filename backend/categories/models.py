from django.db import models
from ckeditor.fields import RichTextField 


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    
    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    text = RichTextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.title