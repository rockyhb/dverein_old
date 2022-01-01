from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Mitgliedskonto(models.Model):
    abrechnungslauf = ForeignKey('Abrechnungslauf', null=True, on_delete=CASCADE)
    mitglied = ForeignKey('Mitglied',null=True, on_delete=CASCADE)
    datum = DateField()
    zweck1 = CharField(null=True, max_length=500)
    zahlungsweg = IntegerField(null=True)
    betrag = FloatField(null=True)
