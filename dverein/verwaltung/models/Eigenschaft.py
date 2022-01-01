from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Eigenschaft(models.Model):
    eigenschaftgruppe = ForeignKey('Eigenschaftgruppe', null=True, on_delete=SET_NULL)
    bezeichnung = CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['bezeichnung','eigenschaftgruppe'], name='ixEigenschaft1')
        ]
