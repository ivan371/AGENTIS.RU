# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0015_auto_20160310_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_data',
            name='img',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
