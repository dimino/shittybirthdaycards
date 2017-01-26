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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('who', models.CharField(max_length=100)),
                ('when', models.DateField()),
                ('street', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=140)),
                ('charge_id', models.CharField(max_length=27, blank=True, null=True)),
            ],
            options={
                'db_table': 'cards',
            },
        ),
    ]
