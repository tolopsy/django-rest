from django.db import models
from django.contrib.auth.models import AbstractUser

import os


'''
Four models
1. User
2. Platform
3. Content
4. Sale
5. Brand
'''

AbstractUser._meta.get_field('email')._unique = True  # Ensures that user's e-mail address is unique

class User(AbstractUser):
    bio = models.TextField(max_length=1000, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)

    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    is_creator = models.BooleanField(default=False)


class Platform(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='platforms', null=True)
    members = models.ManyToManyField(User, related_name='platforms_joined', related_query_name='plaforms_joined', blank=True)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # cover
    cover_image = models.ImageField(null=True, blank=True)

    weekly_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    date_created  = models.DateTimeField(auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date_updated',)


    def __str__(self):
        return self.title 

class Content(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='contents')

    title = models.CharField(max_length=100)
    item = models.FileField(null=True, blank=True)
    description = models.TextField(blank=True)

    is_downloadable = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    date_created  = models.DateTimeField(auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(auto_now=True)

    # one-off price available for users who are not member of related channel but would like to buy content
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    customers = models.ManyToManyField(User, related_name='contents_bought', blank=True) # for one-off content buyers

    class Meta:
        ordering = ('-date_created',)
    
    # obtain the filename without the path
    def content_name(self):
        return os.path.basename(self.item.name)
    
    # return file name and file extension as tuple
    def get_split_name(self):
        return os.path.splitext(self.content_name())
    
    def extension(self):
        split_name = self.get_split_name()
        return split_name[1]



class Sale(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True)

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="purchases")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sales")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sale_id

    class Meta:
        ordering = ('-date_created',)


class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=100,  blank=True)
    is_active = models.BooleanField(default=True)
    phone_number =  models.PositiveIntegerField()
    amount_earned = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)