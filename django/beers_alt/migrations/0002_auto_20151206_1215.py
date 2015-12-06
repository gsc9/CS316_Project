# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('beers_alt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_ingredient',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default='1', serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part_of',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default='1', serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='who_buys',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default='1', serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event_ingredient',
            name='eid',
            field=models.ForeignKey(to='beers_alt.Event', db_column=b'eid'),
        ),
        migrations.AlterField(
            model_name='event_ingredient',
            name='ingredient_name',
            field=models.ForeignKey(to='beers_alt.Ingredient', db_column=b'ingredient_name'),
        ),
        migrations.AlterField(
            model_name='part_of',
            name='eid',
            field=models.ForeignKey(to='beers_alt.Event', db_column=b'eid'),
        ),
        migrations.AlterField(
            model_name='part_of',
            name='email',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'email'),
        ),
        migrations.AlterField(
            model_name='who_buys',
            name='eid',
            field=models.ForeignKey(to='beers_alt.Event', db_column=b'eid'),
        ),
        migrations.AlterField(
            model_name='who_buys',
            name='email',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'email'),
        ),
        migrations.AlterField(
            model_name='who_buys',
            name='ingredient_name',
            field=models.ForeignKey(to='beers_alt.Ingredient', db_column=b'ingredient_name'),
        ),
        migrations.AlterUniqueTogether(
            name='part_of',
            unique_together=set([('email', 'eid')]),
        ),
    ]
