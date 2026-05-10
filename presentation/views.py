# VIEWS.PY 
from django.shortcuts import render
from django.contrib import messages

def home(request):
    print("HOME VIEW KÖRS")
    messages.warning(request, "Uppdatering pågår.")
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def erfarenhet(request):
    return render(request, "erfarenhet.html")

def utbildning(request):
    return render(request, "utbildning.html")

def portfolio(request):
    return render(request, "portfolio.html")

def policy(request):
    return render(request, "policy.html")

def cv(request):
    return render(request, "cv.html")
