from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Spendenbescheinigung(models.Model):
    spendenart = IntegerField(default=1)
    zeile1 = CharField(null=True, max_length=80)
    zeile2 = CharField(null=True, max_length=80)
    zeile3 = CharField(null=True, max_length=80)
    zeile4 = CharField(null=True, max_length=80)
    zeile5 = CharField(null=True, max_length=80)
    zeile6 = CharField(null=True, max_length=80)
    zeile7 = CharField(null=True, max_length=80)
    spendendatum = DateField(null=True)
    bescheinigungsdatum = DateField(null=True)
    beitrag = FloatField(null=True)
    formular = ForeignKey('Formular',null=True,on_delete=SET_NULL)
    ersatzaufwendungen = BooleanField(default=False)
    mitglied = ForeignKey('Mitglied',null=True,on_delete=SET_NULL)
    bezeichnungsachzuweisung = CharField(null=True, max_length=100)
    herkunftspende = IntegerField(null=True)
    unterlagenwertermittlung = BooleanField(default=False)
    autocreate = BooleanField(default=False)
