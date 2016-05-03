# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
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
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
                ('who', models.CharField(max_length=100)),
                ('when', models.DateTimeField()),
                ('street', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='card_uuid',
            field=models.ForeignKey(to='sbc.User', db_column='card_uuid'),
        ),
        migrations.AddField(
            model_name='event',
            name='user_uuid',
            field=models.ForeignKey(to='sbc.Card', db_column='user_uuid'),
        ),
    ]
