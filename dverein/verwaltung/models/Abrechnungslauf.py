from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Abrechnungslauf(models.Model):
    datum = DateField()
    modus = IntegerField()
    faelligkeit = DateField(null=True)
    faelligkeit2 = DateField(null=True)
    stichtag = DateField(null=True)
    eingabedatum = DateField(null=True)
    zahlungsgrund = CharField(max_length=140,null=True)
    zusatzbetraege = BooleanField(default=False)
    kursteilnehmer = BooleanField(default=False)
    dtausdruck = BooleanField(default=False)
    abbuchungsausgabe = IntegerField(null=True)
