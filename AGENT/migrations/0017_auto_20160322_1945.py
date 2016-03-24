# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0016_orders_data_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_data',
            name='img',
            field=models.ForeignKey(to='AGENT.image'),
        ),
    ]
