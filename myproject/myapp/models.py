from django.db import models


# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

PLEC = (
    ('K', 'Kobieta'),
    ('M', 'Mężczyzna'),
    ('I', 'Inne'),
)


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    # skrót Shift + Alt + strzałka góra lub dół - powiela linię, w krórej 
    # znajduje się aktualnie karetka (migający kursor, za którym wpisujemy znaki) 
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        ordering = ['lastname']

# skrót Ctrl + / - dodanie/usunięcie komentarza


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Stanowiska"
    
    def __str__(self):
        return self.nazwa


class Osoba(models.Model):

    imie = models.CharField(max_length=60)    
    nazwisko = models.CharField(max_length=60)  
    data_dodania = models.DateField(auto_now_add=True)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    PLEC = models.CharField(max_length=1, choices=PLEC, null = True)
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.stanowisko})"

    class Meta:
        verbose_name_plural = "Osoby"
