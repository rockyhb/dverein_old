from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Anfangsbestand(models.Model):
    konto = ForeignKey('Konto',null=True,on_delete=SET_NULL)
    datum = DateField(null=True)
    betrag = FloatField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['konto','datum'], name='konto')
        ]
