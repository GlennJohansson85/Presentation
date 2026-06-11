# VIEWS.PY 
from django.shortcuts import render
from django.contrib import messages

def home(request):
    if not request.session.get("home_visited"):
        print("HOME VIEW KÖRS")
        messages.warning(request, "Uppdatering pågår.")
        request.session["home_visited"] = True

    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def experience(request):
    return render(request, "experience.html")

def education(request):
    return render(request, "education.html")

def portfolio(request):
    return render(request, "portfolio.html")

def policy(request):
    return render(request, "policy.html")

def cv(request):
    return render(request, "cv.html")
