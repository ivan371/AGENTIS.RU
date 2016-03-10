# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0014_auto_20160310_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='name_mess',
        ),
        migrations.AlterField(
            model_name='user_agentis',
            name='img',
            field=models.ForeignKey(to='AGENT.image'),
        ),
    ]
