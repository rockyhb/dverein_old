from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Qifimportpos(models.Model):
    headid = ForeignKey('Qifimporthead', on_delete=CASCADE)
    datum = DateField()
    betrag = FloatField()
    beleg = CharField(null=True, max_length=30)
    name = CharField(null=True, max_length=100)
    zweck = CharField(null=True, max_length=100)
    buchartex = CharField(null=True, max_length=50)
    buchart = IntegerField(null=True)
    mitgliedbar = CharField(null=True, max_length=1)
    mitglied = IntegerField(null=True)
    sperre = CharField(null=True, max_length=1)
