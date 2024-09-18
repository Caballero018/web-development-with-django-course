from django.shortcuts import render
from service.models import Service

# Create your views here.
def services(request):
    services = Service.objects.all()

    return render(request=request, template_name="service/services.html", context={"services": services})
