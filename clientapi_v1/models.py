from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Users(models.Model):
    user_id = models.CharField(max_length=17, primary_key=True, unique=True)
    user_name = models.CharField(max_length=15, null=False, unique=True)
    user_email = models.EmailField(null=False,unique=True)
    user_creation_dt = models.DateTimeField(auto_now_add=True)
    user_modify_dt = models.DateTimeField(null=True)
    user_token = models.CharField(max_length=255,blank=True,null=True)

class Admins(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=15, null=False, unique=True)
    user_pass = models.CharField(max_length=256, null=False, unique=True)



class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_category = models.ForeignKey('Categories',on_delete=models.CASCADE)
    item_details = models.TextField(max_length=255)
    item_creation_dt = models.DateTimeField(auto_now_add=True)
    item_update_dt = models.DateTimeField(auto_now=True)
    item_priority = models.IntegerField(default=1)
    item_url = models.URLField(unique=True)
    item_price = models.FloatField()
    # auto_now_true = True, blank = True#

class Categories(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=15,unique=True)

class LikedItems(models.Model):
    user_id = models.ForeignKey('Users',on_delete=models.CASCADE)
    item_id = models.ForeignKey('Items',on_delete=models.CASCADE)
    creation_dt = models.DateTimeField(auto_now_add=True)


