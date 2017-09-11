from django.shortcuts import render

def index(request):
    return render(request,"landing/index.html", {})

def contact(request):
    return render(request,"landing/contact.html", {})