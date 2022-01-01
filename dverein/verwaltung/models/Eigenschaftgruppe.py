from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Eigenschaftgruppe(models.Model):
    bezeichnung = CharField(max_length=30, unique=True)
    pflicht = BooleanField(default=False)
    max1 = BooleanField(default=False)
