from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request=request, template_name="core/index.html")

def about(request):
    return render(request=request, template_name="core/about.html")

def store(request):
    return render(request=request, template_name="core/store.html")

