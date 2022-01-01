from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Adresstyp(models.Model):
    bezeichnung = CharField(null=True,max_length=30, unique=True)
    bezeichnungplural = CharField(null=True,max_length=30)
    jvereinid = IntegerField(null=True)
