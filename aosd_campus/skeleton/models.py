from django.db import models
from django.utils import timezone
from phone_field import PhoneField

# Create your models here.

# Signup form for Connect Page
class ConnectionLink(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True)
    phone = PhoneField(blank=True)
    interest = models.TextField(max_length=2000, blank=True)
    submit_date = models.DateField(blank=True, null=True, default=timezone.now())

    def __str__(self):
        return self.name

# For Leadership Details
class Leader(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = PhoneField(blank=True)
    title = models.CharField(max_length=200)
    profile = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.name

# For Bible Talks
class BibleTalk(models.Model):
    school = models.CharField(max_length=200)
    shorthand = models.CharField(max_length=200)
    info = models.TextField(max_length=1000)
    logo = models.URLField(max_length=1000)

    def __str__(self):
        return self.school

class Resource(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=1000)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class SpecialEvent(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=1000)
    front_graphic = models.ImageField(upload_to='frontpage',blank=True);
    description = models.TextField(max_length=1000)
    visible = models.BooleanField();

    def __str__(self):
        return self.title
