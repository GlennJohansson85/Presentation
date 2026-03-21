from django.urls import path
from django.urls import include, path
from .views import home, contact, about, erfarenhet, utbildning, portfolio, policy


urlpatterns = [
    path("", home, name="home"),
    path("contact.html", contact, name="contact"),
    path("about", about, name="about"),
    path("erfarenhet", erfarenhet, name="erfarenhet"),
    path("utbildning", utbildning, name="utbildning"),
    path("portfolio", portfolio, name="portfolio"),
    path("policy", policy, name="policy"),
    path("__reload__/",include("django_browser_reload.urls")),
]