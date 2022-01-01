from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Kursteilnehmer(models.Model):
    personenart = CharField(null=True, max_length=1)
    anrede = CharField(null=True, max_length=10)
    titel = CharField(null=True, max_length=40)
    name = CharField(null=True, max_length=40)
    vorname = CharField(null=True, max_length=40)
    strasse = CharField(null=True, max_length=40)
    adressierungszusatz = CharField(null=True, max_length=40)
    plz = CharField(null=True, max_length=10)
    ort = CharField(null=True, max_length=40)
    staat = CharField(null=True, max_length=50)
    email = CharField(null=True, max_length=50)
    bic = CharField(null=True, max_length=11)
    iban = CharField(null=True, max_length=34)
    vzweck1 = CharField(null=True, max_length=140)
    mandatdatum = DateField(null=True)
    blz = CharField(null=True, max_length=8)
    konto = CharField(null=True, max_length=12)
    betrag = FloatField()
    geburtsdatum = DateField(null=True)
    geschlecht = CharField(null=True, max_length=1)
    eingabedatum = DateField()
    abbudatum = DateField(null=True)
