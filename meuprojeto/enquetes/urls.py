from django.urls import path

from . import views

urlpatterns = [
    path('bemvindo/',views.welcome),
]