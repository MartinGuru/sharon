import email
from unicodedata import name
from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactsharon(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')

        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.save()
        return HttpResponse("<h3>Thank you! we will get back to you shortly</h3>")
    return render(request, 'contactsharon.html')

def historysharon(request):
    return render(request, 'historysharon.html')

def sharondesigners(request):
    return render(request, 'sharondesigners.html')

def sharonfaceart(request):
    return render(request, 'sharonfaceart.html')

def sharonstylists(request):
    return render(request, 'sharonstylists.html')                    