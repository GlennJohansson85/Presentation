from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def erfarenhet(request):
    return render(request, "erfarenhet")

def utbildning(request):
    return render(request, "utbildning")

def portfolio(request):
    return render(request, "portfolio.html")

def policy(request):
    return render(request, "policy.html")

def cv(request):
    return render(request, "cv.html")
