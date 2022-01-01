from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Beitragsgruppe(models.Model):
    bezeichnung = CharField(max_length=30)
    betrag = FloatField(null=True)
    beitragsart = IntegerField(null=True)
    arbeitseinsatzstunden = FloatField(null=True)
    arbeitseinsatzbetrag = FloatField(null=True)
    buchungsart = ForeignKey('Buchungsart',null=True,on_delete=SET_NULL)
    betragmonatlich = FloatField(null=True)
    betragvierteljaehrlich = FloatField(null=True)
    betraghalbjaehrlich = FloatField(null=True)
    betragjaehrlich = FloatField(null=True)
