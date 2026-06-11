from django.urls import path
from django.urls import include, path
from .views import home, contact, about, experience, education, portfolio, policy, cv


urlpatterns = [
    path("", home, name="home"),
    path("contact.html", contact, name="contact"),
    path("about", about, name="about"),
    path("experience", experience, name="experience"),
    path("education", education, name="education"),
    path("portfolio", portfolio, name="portfolio"),
    path("cv", cv, name="cv"),
    path("policy", policy, name="policy"),
    path("__reload__/",include("django_browser_reload.urls")),
]