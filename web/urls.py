from django.urls import path
from . import views 


app_name = 'web'

urlpatterns = [
    path("",views.index, name='index'),
    path('users/', views.users, name='users'),
    path('set_delete/<int:user_id>/', views.set_delete, name='set_delete'),
]

