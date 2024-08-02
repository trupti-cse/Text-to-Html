from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('converter.urls')),  # Redirect root URL to the login page
    path('', include('converter.urls')),          # Include all URLs from the converter app
]
