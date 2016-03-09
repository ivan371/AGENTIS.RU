# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0009_order_href_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_agentis',
            name='img',
            field=models.ImageField(default=0, upload_to=b''),
        ),
    ]
