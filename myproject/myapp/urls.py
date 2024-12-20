from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("welcome", views.welcome_view),
    path("personds", views.person_list),
    # path("person/<int:id>", views.person_detail)
]

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('myapp/', include('myapp.urls')), # dołączamy reguły url z pliku myapp\urls.py
    path('admin/', admin.site.urls),
]

