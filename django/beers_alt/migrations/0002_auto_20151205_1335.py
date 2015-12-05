# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers_alt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_ingredient',
            name='name',
            field=models.ForeignKey(to='beers_alt.Ingredient', db_column=b'ingredient_name'),
        ),
    ]
