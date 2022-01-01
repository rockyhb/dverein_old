from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Konto(models.Model):
    nummer = CharField(null=True, max_length=35, unique=True)
    bezeichnung = CharField(null=True, max_length=255)
    eroffnung = DateField(null=True)
    aufloesung = DateField(null=True)
    hibiscusid = IntegerField(null=True)
