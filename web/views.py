from django.shortcuts import render , reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User 

from .models import user

from .resources import PersonResource
from tablib import Dataset
import pandas as pd


def clean_phone(phone):
    return ''.join(filter(str.isdigit, str(phone)))

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        excel_file = request.FILES['myfile']
        df = pd.read_excel(excel_file)
        
        # Assuming 'Name', 'Phone', and 'Email' are required columns in the Excel sheet
        required_columns = ['Name', 'Phone', 'Email']
        
        # Check if all required columns exist in the Excel sheet
        if all(col in df.columns for col in required_columns):
            # Process the data and save it to your Django model
            for index, row in df.iterrows():
                name = row['Name']
                raw_phone = row['Phone'] 
                phone = clean_phone(raw_phone)  
                email = row['Email']
                
                # Create a new instance of the 'user' model and save it to the database
                new_user = user(name=name, phone=phone, email=email)
                new_user.save()
                
            # Data processing completed
            return HttpResponseRedirect("users")
        else:
            # Handle missing columns
            missing_columns = [col for col in required_columns if col not in df.columns]
            return HttpResponse(f"Missing columns: {missing_columns}", status=400)
    
    return render(request, 'index.html') 


def users(request):
    users = user.objects.filter(is_delete=False)
    context = {
            "title":"Contact | users",
            "users":users,

    }
    
    return render(request,"users/users.html",context=context)


def set_delete(request, user_id): 
    user = get_object_or_404(User, id=user_id)  
    user.is_delete = True
    user.save()

    return HttpResponseRedirect(reverse('users'))

