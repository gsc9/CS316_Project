# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.models import User
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drinker',
            fields=[
                ('name', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eid', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=400, null=True, blank=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Event_Ingredient',
            fields=[
                ('ingredient_name', models.ForeignKey(to='beers_alt.Ingredient', db_column=b'ingredient_name', primary_key=True)),
                ('eid', models.ForeignKey(to='beers_alt.Event', db_column=b'eid')),
                ('quantity', models.IntegerField()),
                ('units', models.CharField(max_length=256)),
                ('comments', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'event_ingredient',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_name', models.CharField(max_length=256, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'ingredient',
            },
        ),
        migrations.CreateModel(
            name='Part_Of',
            fields=[
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'uid', primary_key=True)),
                ('eid', models.ForeignKey(to='beers_alt.Event', db_column=b'eid')),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'part_of',
            },
        ),
        migrations.CreateModel(
            name='Registered_User',
            fields=[
                ('email', models.CharField(max_length=256, serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'registered_user',
            },
        ),
        migrations.CreateModel(
            name='Who_Buys',
            fields=[
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'uid', primary_key=True)),
                ('ingredient_name', models.ForeignKey(to='beers_alt.Ingredient', db_column=b'ingredient_name', primary_key=True)),
                ('eid', models.ForeignKey(to='beers_alt.Event', db_column=b'eid', primary_key=True)),
                ('bringing', models.IntegerField()),
                ('user_comments', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'who_buys',
            },
        ),
    ]
