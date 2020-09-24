from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name="homepage"),
    path('clients/',clients,name="clients"),
    path('vendors/',vendors,name="vendors"),
    path('about-us/',aboutus,name="about"),
    path('contact-us/',contactus,name="contact"),
]