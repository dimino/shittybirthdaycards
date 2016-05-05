# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('background', models.FilePathField()),
            ],
            options={
                'db_table': 'cards',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('who', models.CharField(max_length=100)),
                ('when', models.DateTimeField()),
                ('street', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=140)),
                ('card_uuid', models.ForeignKey(to='sbc.Card', db_column='card_uuid')),
                ('user_uuid', models.ForeignKey(to='sbc.Account', db_column='user_uuid')),
            ],
            options={
                'db_table': 'events',
            },
        ),
    ]
