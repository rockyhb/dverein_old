from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Qifimporthead(models.Model):
    name = CharField(null=True, max_length=30)
    beschreibung = CharField(null=True, max_length=30)
    startsaldo = FloatField(null=True)
    startdate = DateField(null=True)
    konto = IntegerField(null=True)
    importdatum = DateField()
    importfile = CharField(null=True, max_length=256)
    processdate = DateField(null=True)
