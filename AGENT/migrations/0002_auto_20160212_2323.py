# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_AGENTIS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('who', models.IntegerField(default=0)),
                ('login', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('forename', models.CharField(max_length=30)),
                ('partronyname', models.CharField(max_length=30)),
                ('region', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=30)),
                ('number', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=3000)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
