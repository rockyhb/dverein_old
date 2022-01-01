from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.lookups import In

class Mitgliedfoto(models.Model):
    mitglied = OneToOneField('Mitglied', null=True, on_delete=CASCADE)
    foto = BinaryField(null=True)
