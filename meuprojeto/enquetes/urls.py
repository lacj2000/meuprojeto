from django.urls import path

from . import views

urlpatterns = [
    path('bemvindo/',views.welcome),
    path('enquete/<int:enquete_id>',views.exibir_enquete),
]