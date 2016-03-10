# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0013_delete_mediamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_mess', models.CharField(default=0, max_length=3000)),
                ('img', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='name_mess',
            field=models.ForeignKey(default=0, to='AGENT.image'),
            preserve_default=False,
        ),
    ]
