from django.contrib import admin
from .models import Recipe_Category,Recipe, UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Recipe_Category)
admin.site.register(Recipe)