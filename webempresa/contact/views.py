from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["alejoxcaballero18@gmail.com"],                
                reply_to=[email]
            )
            
            try:
                email.send()
                return redirect(reverse("contact") + "?ok")
            except:
                return redirect(reverse("contact") + "?false")
            
    return render(request=request, template_name="contact/contact.html", context={"form": contact_form})
