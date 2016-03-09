# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0012_mediamodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MediaModel',
        ),
    ]
