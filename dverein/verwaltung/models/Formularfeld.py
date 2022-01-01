from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Formularfeld(models.Model):
    formular = ForeignKey('Formular', null=True, on_delete=CASCADE)
    name = CharField(null=True, max_length=60)
    seite = IntegerField(null=True)
    x = FloatField(null=True)
    y = FloatField(null=True)
    font = CharField(null=True, max_length=50)
    fontsize = IntegerField(null=True)
    fontstyle = IntegerField(null=True)
