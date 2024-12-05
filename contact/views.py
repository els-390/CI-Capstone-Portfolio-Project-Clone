from django.shortcuts import render
from django.http import HttpResponse
from reviews.models import ContactForm

# Create your views here.

def Contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contact': contact})
