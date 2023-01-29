from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "websiteapp/home.html")
def products(request):
    return render(request, "websiteapp/products.html")
def people(request):
    return render(request, "websiteapp/people.html")
def contactus(request):
    return render(request,"websiteapp/contactus.html")
    