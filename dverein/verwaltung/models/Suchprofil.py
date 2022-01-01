from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Suchprofil(models.Model):
    bezeichnung = CharField(null=True, max_length=50)
    inhalt = BinaryField(null=True)
    clazz = CharField(null=True, max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['bezeichnung','clazz'], name='ixSuchprofil1')
        ]
