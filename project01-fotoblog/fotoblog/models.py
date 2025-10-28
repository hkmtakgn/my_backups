from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class BaseModel (models.Model):
    title = models.CharField (max_length=100,blank=False,null=False)
    slug = AutoSlugField (populate_from="title")
    content = models.TextField (blank=True,null=True)
    img = models.ImageField (upload_to="page_img/")
    is_active = models.BooleanField (default=True)

    class Meta:
        abstract = True


class Page (BaseModel):

    def __str_ (self):
        return self.title
    

class Post (BaseModel):
    user = models.ForeignKey (User,on_delete=models.CASCADE,blank=False,null=False)
    
    def __str__ (self):
        return self.title
    