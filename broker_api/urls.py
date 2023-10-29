"""
URL configuration for broker_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from notes.views import NotesViewSet

# Notes routes
notes_router = routers.SimpleRouter()
notes_router.register(r"notes", NotesViewSet, basename="note")

urlpatterns = [
    path("admin/", admin.site.urls),
    # Notes router for CRUD
    path("api/", include(notes_router.urls)),
    # Customer Routes
    path("customer/", include('notes.urls'))
]
