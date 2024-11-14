# Generated by Django 5.1.3 on 2024-11-14 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('plec', models.CharField(choices=[('K', 'Kobieta'), ('M', 'Mezczyzna'), ('I', 'Inni')], default='K', max_length=1)),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stanowisko')),
            ],
        ),
    ]