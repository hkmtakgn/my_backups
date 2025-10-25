from django.db import models
from autoslug import AutoSlugField




class Page (models.Model):
    title = models.CharField (max_length=100,blank=False,null=False)
    slug = AutoSlugField (populate_from="title")
    content = models.TextField (blank=True,null=True)
    page_img = models.ImageField (upload_to="page_img/")
    is_active = models.BooleanField (default=True)

    def __str_ (self):
        return self.title
    
