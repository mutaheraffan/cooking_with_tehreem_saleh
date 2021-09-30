from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('add',views.add, name = "add"),
    path('recipe_details/<recipe_id>/',views.recipe_details, name = "recipe_details"),
    path('download_recipe/<recipe_id>/',views.download_recipe, name = "download_recipe"),
    path('send_message/', views.send_message, name= "send_message"),
]