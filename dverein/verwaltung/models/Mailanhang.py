from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import BinaryField, BooleanField, CharField, DateField, DateTimeField, FloatField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import In

class Mailanhang(models.Model):
    mail = ForeignKey('Mail', on_delete=CASCADE)
    anhang = BinaryField(null=True)
    dateiname = CharField(null=True, max_length=50)
