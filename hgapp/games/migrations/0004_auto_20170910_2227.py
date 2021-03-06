# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20170906_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_attendance',
            name='outcome',
            field=models.CharField(blank=True, choices=[('WIN', 'Win'), ('LOSS', 'Loss'), ('DEATH', 'Death'), ('DECLINED', 'Declined Harbinger Invite'), ('RINGER_VICTORY', 'Ringer Victory'), ('RINGER_FAILURE', 'Ringer Failure')], max_length=20, null=True),
        ),
    ]
