# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('beers_alt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part_of',
            name='eid',
            field=models.ForeignKey(to='beers_alt.Event', db_column=b'eid'),
        ),
        migrations.AlterField(
            model_name='part_of',
            name='uid',
            field=models.ForeignKey(primary_key=True, db_column=b'uid', serialize=False, to='beers_alt.Registered_User'),
        ),
        migrations.AlterField(
            model_name='who_buys',
            name='eid',
            field=models.ForeignKey(to='beers_alt.Event', db_column=b'eid'),
        ),
        migrations.AlterField(
            model_name='who_buys',
            name='ingredient_name',
            field=models.ForeignKey(to='beers_alt.Ingredient', db_column=b'ingredient_name'),
        ),
        migrations.AlterField(
            model_name='who_buys',
            name='uid',
            field=models.ForeignKey(primary_key=True, db_column=b'uid', serialize=False, to='beers_alt.Registered_User'),
        ),
        migrations.AlterUniqueTogether(
            name='part_of',
            unique_together=set([('uid', 'eid')]),
        ),
    ]
