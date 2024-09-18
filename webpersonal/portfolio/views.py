from django.shortcuts import render
from portfolio.models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    return render(request=request, template_name="portfolio/portfolio.html", context={'projects': projects})
