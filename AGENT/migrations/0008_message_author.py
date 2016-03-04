# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0007_auto_20160223_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.IntegerField(default=0),
        ),
    ]
