# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0008_message_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='href_order',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
