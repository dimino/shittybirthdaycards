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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('who', models.CharField(max_length=100)),
                ('when', models.DateTimeField()),
                ('street', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'cards',
            },
        ),
    ]
