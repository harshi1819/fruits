from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def redie(request):
    return HttpResponse('Apples and Cherry are red')