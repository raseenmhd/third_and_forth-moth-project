from django.urls import path
from user.views import users


app_name = 'user'

urlpatterns = [
    path("", users, name='users'),
]
