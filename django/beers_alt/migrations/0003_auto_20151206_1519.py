# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers_alt', '0002_auto_20151206_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_user',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
