# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0004_auto_20160217_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_mess', models.CharField(max_length=100)),
                ('sum_mess', models.IntegerField(default=0)),
                ('message', models.CharField(max_length=3000)),
                ('user_m', models.ForeignKey(to='AGENT.User_AGENTIS')),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='user_m',
        ),
        migrations.DeleteModel(
            name='orders',
        ),
    ]
