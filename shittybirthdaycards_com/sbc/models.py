import datetime
from django.db import models


class Card(models.Model):
    who = models.CharField(max_length=100)
    when = models.DateField()

    street = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=11)

    message = models.CharField(max_length=140)

    charge_id = models.CharField(max_length=27, null=True, blank=True)

    class Meta:
        db_table = 'cards'
