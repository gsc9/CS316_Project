# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers_alt', '0002_auto_20151205_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_ingredient',
            old_name='name',
            new_name='ingredient_name',
        ),
        migrations.RemoveField(
            model_name='who_buys',
            name='name',
        ),
        migrations.AddField(
            model_name='who_buys',
            name='ingredient_name',
            field=models.ForeignKey(db_column=b'ingredient_name', default='blah', to='beers_alt.Ingredient'),
            preserve_default=False,
        ),
    ]
