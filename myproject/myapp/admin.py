from django.contrib import admin

# Register your models here.

from .models import Osoba, Stanowisko

admin.site.register(Stanowisko)
admin.site.register(Osoba)
