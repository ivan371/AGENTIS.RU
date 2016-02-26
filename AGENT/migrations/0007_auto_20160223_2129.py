# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGENT', '0006_messages_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0)),
                ('message', models.CharField(max_length=3000)),
                ('mess_from', models.ForeignKey(related_name='mess_from', to='AGENT.User_AGENTIS')),
                ('mess_to', models.ForeignKey(related_name='mess_to', to='AGENT.User_AGENTIS')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0)),
                ('order_from', models.ForeignKey(related_name='order_from', to='AGENT.User_AGENTIS')),
                ('order_to', models.ForeignKey(related_name='order_to', to='AGENT.User_AGENTIS')),
            ],
        ),
        migrations.DeleteModel(
            name='messages',
        ),
        migrations.DeleteModel(
            name='orders',
        ),
    ]
