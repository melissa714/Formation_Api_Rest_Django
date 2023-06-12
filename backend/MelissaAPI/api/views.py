from django.shortcuts import render
from  django.http import JsonResponse 
import json
# Create your views here.



# def api_view(request,*args,**kwargs):
#     # instance de http request 
#     # request => httpRequest 
#     print(request)
#     data={
#         'name':'melissa',
#         'language':'python',

#     }
#     return JsonResponse(data)





# def api_view(request,*args,**kwargs):
#     # instance de http request 
#     # request => httpRequest 
#     print(request.body) # le body renvoie un byte string
#     data=json.loads(request.body)
#     pre_data=json.dumps(data)
#     print(pre_data)
#     print(data)
#     data['headers']=dict(request.headers)
#     data['params']=dict(request.GET)
#     data['post-data']=dict(request.POST)
#     print(request.headers)
#     data['content_type']=request.content_type
#     return JsonResponse(data)





def api_view(request,*args,**kwargs):
    data={

        'name':'melissa',
        'language':'python',

    }
    return JsonResponse(data)