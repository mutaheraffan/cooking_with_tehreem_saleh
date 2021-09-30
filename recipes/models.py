from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
import os
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    user   = models.OneToOneField(User,on_delete=models.CASCADE)
    ProfilePhoto = models.ImageField(upload_to='User_Profiles')
    designation = models.CharField(max_length=150)
    twitter_link = models.CharField(max_length=250)
    facebook_link = models.CharField(max_length=250)
    instagram_link = models.CharField(max_length=250)
    linkedin_link = models.CharField(max_length=250)

    def __str__(self):
        return self.user.email

    def extension(self):
        name, extension = os.path.splitext(self.ProfilePhoto.name)
        return extension


class Recipe_Category(models.Model):
    category_id =   models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name =_("Recipe Category")
        verbose_name_plural = ("Recipe Categories")

    def __str__(self):
        return self.category_name + " Category"


class Recipe(models.Model):
    recipe_category = models.ForeignKey(Recipe_Category, 
                                        verbose_name=_("Recipe Category"), 
                                        blank=False, 
                                        null=False, 
                                        on_delete= models.CASCADE)
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    recipe_pic = models.ImageField(upload_to='pics')
    short_description = models.TextField()
    ingredients = models.TextField()
    recipe_details = models.TextField()
    author = models.CharField(max_length=100)
    recipe_by = models.CharField(max_length=100)
    video_link = models.CharField(max_length=250)
    special = models.BooleanField(default=False)
    publish_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name =_("Recipe Details")
        verbose_name_plural = ("Recipes Details")
    
    def __str__(self):
        return self.title + " Recipe"

