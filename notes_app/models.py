from django.db import models
from django.contrib.auth.models import User
import datetime #this django date , but the tags date is python data
from django.utils.text import slugify

# Create your models here.

class Notes(models.Model):
    """docstring for Notes."""
    user       = models.ForeignKey(User , on_delete=models.CASCADE)
    title      = models.CharField(max_length=50)
    slug       = models.SlugField(null = True , blank=True)
    content    = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True , default=datetime.datetime.now)
    active     = models.BooleanField(default=True)
    tags = models.CharField(blank=True  , max_length=100)

    def save(self , *args , **Kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Notes , self).save( *args , **Kwargs)

    def __str__(self):
        return self.title
