from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Buchung(models.Model):
    umsatzid = IntegerField(null=True)
    konto = ForeignKey('Konto',null=True,on_delete=SET_NULL)
    auszugsnummer = IntegerField(null=True)
    blattnummer = IntegerField(null=True)
    name = CharField(null=True, max_length=100)
    betrag = FloatField()
    zweck = CharField(null=True, max_length=500)
    datum = DateField()
    art = CharField(null=True, max_length=100)
    kommentar = CharField(null=True, max_length=1000)
    buchungsart = ForeignKey('Buchungsart',null=True,on_delete=SET_NULL)
    mitgliedskonto = ForeignKey('Mitgliedskonto',null=True,on_delete=SET_NULL)
    abrechnungslauf = ForeignKey('Abrechnungslauf', null=True, on_delete=models.SET_NULL)
    splitid = IntegerField(null=True)
    splittyp = IntegerField(null=True)
    spendenbescheinigung = ForeignKey('Spendenbescheinigung',null=True,on_delete=SET_NULL)
    verzicht = BooleanField(default=False)
    projekt = ForeignKey('Projekt',null=True,on_delete=SET_NULL)
