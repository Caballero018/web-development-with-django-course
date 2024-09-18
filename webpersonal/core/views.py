from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request=request, template_name="core/home.html")

def about(request):
    return render(request=request, template_name="core/about.html")

def contact(request):
    return render(request=request, template_name="core/contact.html")
