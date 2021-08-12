from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('payment/',order,name='payment'),
    path('thx/',thx, name='thanks')
]