# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('partronyname', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('number', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=3000)),
            ],
        ),
    ]
