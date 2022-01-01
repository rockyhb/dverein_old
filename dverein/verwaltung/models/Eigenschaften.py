from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Eigenschaften(models.Model):
    mitglied = ForeignKey('Mitglied', null=True, on_delete=CASCADE)
    eigenschaft = ForeignKey('Eigenschaft', null=True, on_delete=CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['mitglied','eigenschaft'], name='ixEigenschaften1')
        ]
