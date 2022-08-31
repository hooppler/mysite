from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    #return HttpResponse('Hello World!!!')
    return render(request, 'base_app/home.html')
