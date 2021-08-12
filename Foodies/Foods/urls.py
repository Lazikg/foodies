from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('products/', Products.as_view(), name='products'),
    path('category/<str:cid>',Category_Products.as_view(), name='c_p')
]   

