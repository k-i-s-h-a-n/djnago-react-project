from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.



def homepage(request):
    return JsonResponse('Hello Kishan',safe=False)