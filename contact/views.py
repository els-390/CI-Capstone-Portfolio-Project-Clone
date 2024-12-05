from django.shortcuts import render
from django.http import HttpResponse
from about.models import ContactRequest

# Create your views here.

def contact(request):
    return render(request, 'contact.html', {'contact': contact})