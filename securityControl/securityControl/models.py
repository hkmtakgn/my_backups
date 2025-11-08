from enum import unique
from django.core import validators
from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

# Create your models here.

tc_validator = RegexValidator(
    regex=r'^[1-9][0-9]{10}$',
    message="TC Kimlik Numarası 11 haneli olmalı ve 0 ile başlamamalıdır.")


class BaseModel(models.Model):
  first_name = models.CharField(max_length=100, null=False, blank=False)
  last_name = models.CharField(max_length=100, null=False, blank=False)
  tc_kimlik_no = models.CharField(max_length=11,
                                  null=False,
                                  blank=False,
                                  unique=True,
                                  validators=[tc_validator])

  class Meta:
    abstract = True


class Page(models.Model):
  title = models.CharField(max_length=100,
                           unique=True,
                           blank=False,
                           null=False)
  slug = models.SlugField(max_length=120, unique=True, null=False, blank=True)
  img = models.ImageField(upload_to="page_img/")
  is_active = models.BooleanField(default=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.title


class Ziyaretci(BaseModel):

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class Taseron(models.Model):
  ziyaretci = models.ForeignKey(Ziyaretci,
                                on_delete=models.CASCADE,
                                blank=False,
                                null=False)
  firma_adi = models.CharField(max_length=100)
  davet_eden = models.CharField(max_length=100)
  yapilacak_is = models.CharField(max_length=100)
  calisma_alani = models.CharField(max_length=100)
  is_inside = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.firma_adi


class yuk_arac(models.Model):
  sofor = models.ForeignKey(Ziyaretci,
                            on_delete=models.CASCADE,
                            null=False,
                            blank=False)
  cekici_plaka = models.CharField(max_length=100,
                                  null=False,
                                  blank=False,
                                  unique=True)
  dorse_plaka = models.CharField(max_length=100,
                                 null=False,
                                 blank=False,
                                 unique=True)
  firma_adi = models.CharField(max_length=100, null=False, blank=False)
  arac_turu = models.CharField(max_length=100, null=False, blank=False)
  sevkiyat_bolumu = models.CharField(max_length=100, null=False, blank=False)
  gidecegi_yer = models.CharField(max_length=100, null=False, blank=False)
  aciklama = models.TextField(blank=True, null=True)
  is_inside = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
