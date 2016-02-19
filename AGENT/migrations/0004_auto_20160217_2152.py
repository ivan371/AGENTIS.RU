# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0003_remove_user_agentis_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_mess', models.CharField(max_length=100)),
                ('sum_mess', models.IntegerField(default=0)),
                ('message', models.CharField(max_length=3000)),
            ],
        ),
        migrations.AddField(
            model_name='user_agentis',
            name='prof',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='user_m',
            field=models.ForeignKey(to='AGENT.User_AGENTIS'),
        ),
    ]
