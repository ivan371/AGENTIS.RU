# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0011_auto_20160304_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_file', models.FileField(upload_to=b'user_media')),
            ],
        ),
    ]
