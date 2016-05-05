from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True)

    class Meta:
        abstract = True


class Account(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'users'


class Card(BaseModel):
    name = models.CharField(max_length=100)
    background = models.FilePathField()

    class Meta:
        db_table = 'cards'


class Event(BaseModel):
    who = models.CharField(max_length=100)
    when = models.DateTimeField()

    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=11)

    message = models.CharField(max_length=140)

    card_uuid = models.ForeignKey(Card, db_column='card_uuid')
    user_uuid = models.ForeignKey(Account, db_column='user_uuid')

    class Meta:
        db_table = 'events'
