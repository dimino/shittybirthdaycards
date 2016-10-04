from django.db import models


class Card(models.Model):
    who = models.CharField(max_length=100)
    when = models.DateTimeField()

    street = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=11)

    message = models.CharField(max_length=140)

    class Meta:
        db_table = 'cards'
