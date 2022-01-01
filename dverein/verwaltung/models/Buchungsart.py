from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Buchungsart(models.Model):
    nummer = IntegerField(null=True, unique=True)
    bezeichnung = CharField(null=True, max_length=50)
    art = IntegerField(null=True)
    buchungsklasse = ForeignKey('Buchungsklasse', null=True, on_delete=SET_NULL)
    spende = BooleanField(default=False)
