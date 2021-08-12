from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('login/',LoginUser.as_view(), name='login'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    
]