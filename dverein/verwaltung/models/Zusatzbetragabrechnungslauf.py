from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, DecimalField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Zusatzbetragabrechnungslauf(models.Model):
    abrechnungslauf = ForeignKey('Abrechnungslauf', null=True, on_delete=CASCADE)
    zusatzbetrag = ForeignKey('Zusatzabbuchung', null=True, on_delete=CASCADE)
    letzteausfuehrung = DateField(null=True)
