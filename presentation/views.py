# VIEWS.PY 
from django.shortcuts import render
from django.contrib import messages

def home(request):
    if not request.session.get("home_visited"):
        print("HOME VIEW KÖRS")
        messages.warning(request, "Uppdatering pågår.")
        request.session["home_visited"] = True

    return render(request, "home.html")
