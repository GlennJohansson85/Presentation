from django.urls import path
from django.urls import include, path
from .views import home


urlpatterns = [
    path("", home, name="home"),
    path("__reload__/",include("django_browser_reload.urls")),
]