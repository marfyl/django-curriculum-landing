"""marfylaso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = []

if settings.ADMIN_PANEL_ACTIVE:
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]

urlpatterns += [
    path('', include('landing.urls', namespace='landing')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
