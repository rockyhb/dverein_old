from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, DecimalField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Zusatzfelder(models.Model):
    mitglied = ForeignKey('Mitglied', null=True, on_delete=CASCADE)
    felddefinition = ForeignKey('Felddefinition', null=True, on_delete=CASCADE)
    feld = CharField(null=True, max_length=1000)
    felddatum = DateField(null=True)
    feldganzzahl = IntegerField(null=True)
    feldgleitkommazahl = FloatField(null=True)
    feldwaehrung = DecimalField(null=True, max_digits=15, decimal_places=2)
    feldjanein = BooleanField(null=True)
