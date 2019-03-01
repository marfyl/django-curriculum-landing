from django.urls import path

from .views import LandingView

app_name = 'landing'

urlpatterns = [
    path('', LandingView.as_view(), name='index'),
]
