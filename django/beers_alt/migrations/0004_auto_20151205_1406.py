# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers_alt', '0003_auto_20151205_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
    ]
