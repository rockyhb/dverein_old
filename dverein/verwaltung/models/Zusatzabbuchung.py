from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Zusatzabbuchung(models.Model):
    mitglied = ForeignKey('Mitglied', null=True, on_delete=SET_NULL)
    faelligkeit = DateField()
    buchungstext = CharField(null=True, max_length=140)
    betrag = FloatField()
    startdatum = DateField()
    intervall = IntegerField(null=True)
    endedatum = DateField(null=True)
    ausfuehrung = DateField(null=True)
