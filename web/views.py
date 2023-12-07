from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    context = {
        "title": "Contat | Home",
    }
    return render(request,'index.html', context=context)
