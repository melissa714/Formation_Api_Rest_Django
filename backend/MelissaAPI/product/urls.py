from django.urls import path  
from product.views import *


urlpatterns = [
    path('',api_view,name='api_view'),
]

