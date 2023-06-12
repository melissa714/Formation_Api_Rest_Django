from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict 
# Create your views here.

# def api_view(request):
#     query = Product.objects.all().order_by('?').first()
#     #requete qui retourn resultat de façon aléatoire
#     data={}
#     #si le query exist 
#     if query:
#         data['name']=query.name
#         data['content']=query.content
#         data['price']=query.price
#         #serrialization :mettre les données sous forme de dictionnaire 
#     return JsonResponse(data)   






def api_view(request):
    query = Product.objects.all().order_by('?').first()
    #requete qui retourn resultat de façon aléatoire
    data={}
    #si le query exist 
    if query:
        data= model_to_dict(query)
        # model_to_dict convertir django model en dictionnaire 
        #serialization :mettre les données sous forme de dictionnaire 
    return JsonResponse(data)   