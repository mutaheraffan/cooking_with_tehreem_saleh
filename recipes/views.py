import re
from django.db.models.query import QuerySet
from django.http.response import BadHeaderError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from twilio.rest.api.v2010.account import message
from .models import Recipe_Category,Recipe
from django.contrib.auth import get_user_model
#Below Imports are for generating PDF and Showing Download Notification
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from twilio.rest import Client
import os
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    recipe_categories = Recipe_Category.objects.all()
    recipes = Recipe.objects.all()
    all_users = get_user_model().objects.all()
    recent_recipes = Recipe.objects.all().order_by('-recipe_id')
    return render(request, 'index.html', {'recipe_categories':recipe_categories,'recipes':recipes, 'all_users' : all_users, 'recent_recipes' : recent_recipes})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val1 + val2
    return render(request, 'result.html',{'result': result})

def recipe_details(request,recipe_id):
    recipe_details = Recipe.objects.get(recipe_id=recipe_id)
    return render(request, 'recipe.html', {'recipe_details':recipe_details})

def download_recipe(request,recipe_id):
    recipe_details = Recipe.objects.get(recipe_id=recipe_id)
    
    lines = []
    
    lines.append(recipe_details.title)
    lines.append(recipe_details.short_description)
    lines.append(recipe_details.ingredients)
    lines.append(recipe_details.recipe_details)

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFont('Helvetica-Bold', 15)
    p.drawString(250, 800, recipe_details.title)
    p.setFont('Helvetica-Bold', 6)
    p.drawString(10, 730, "Short Description")
    p.drawString(60, 710, recipe_details.short_description)
    p.drawString(10, 680, "Ingredients")
    p.drawString(60, 650, recipe_details.ingredients)
    p.drawString(10, 620, "Procedure")
    p.drawString(60, 590, recipe_details.recipe_details)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=recipe_details.title+' Recipe.pdf')

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        }

        message = '''
        New message: {}

        From: {}
        '''.format(data['message'],data['email'])
        try:
            send_mail(
                data['subject'], 
                message, 
                'cookingwebsite3@gmail.com',
                 ['tahreemfatima273@gmail.com'],
                 fail_silently=False
                 )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request,'Message sent successfully')
        return redirect("/")

    else:
        return render(request,"/",)