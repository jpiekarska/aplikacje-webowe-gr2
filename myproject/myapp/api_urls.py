from django.urls import path, include
from . import api_views

urlpatterns = [
    path('persons/', api_views.person_list),
    # tu oczekujemy przekazania parametru typu int
    # który będzie w tym widoku dostępny poprzez zmienną o nazwie pk
    path('persons/<int:pk>/', api_views.person_detail),
]