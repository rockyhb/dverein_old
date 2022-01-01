from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Lastschrift(models.Model):
    abrechnungslauf = ForeignKey('Abrechnungslauf', null=True, on_delete=CASCADE)
    mitglied = ForeignKey('Mitglied', null=True, on_delete=SET_NULL)
    kursteilnehmer = ForeignKey('Kursteilnehmer', null=True, on_delete=SET_NULL)
    personenart = CharField(null=True, max_length=1)
    anrede = CharField(null=True, max_length=40)
    titel = CharField(null=True, max_length=40)
    name = CharField(max_length=40)
    vorname = CharField(null=True, max_length=40)
    strasse = CharField(null=True, max_length=40)
    adressierungszusatz = CharField(null=True, max_length=40)
    plz = CharField(null=True, max_length=10)
    ort = CharField(null=True, max_length=40)
    staat = CharField(null=True, max_length=50)
    email = CharField(null=True, max_length=50)
    mandatid = CharField(max_length=35)
    mandatdatum = DateField()
    mandatsequence = CharField(null=True, max_length=4)
    bic = CharField(max_length=11)
    iban = CharField(max_length=35)
    verwendungszweck = CharField(max_length=140)
    betrag = FloatField()
    geschlecht = CharField(null=True, max_length=1)
