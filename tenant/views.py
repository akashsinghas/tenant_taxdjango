from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
def registration(request):
    return render(request,'registration.html')
def home(request):
    return render(request,'home.html')
def property_tax(request):
    return render(request,'property_tax.html')
