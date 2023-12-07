from django.shortcuts import render

def users(request):
    context = {
        "title": "Contat | User",
    }
    return render(request,'users/users.html', context=context)