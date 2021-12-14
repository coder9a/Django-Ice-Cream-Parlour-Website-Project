from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")