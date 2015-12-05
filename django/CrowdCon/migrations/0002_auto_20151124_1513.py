# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrowdCon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eid', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Event_Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('units', models.CharField(max_length=256)),
                ('comments', models.CharField(max_length=256)),
                ('eid', models.ForeignKey(to='CrowdCon.Event', db_column=b'eid')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('eid', models.ForeignKey(to='CrowdCon.Event', db_column=b'eid')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bringing', models.IntegerField()),
                ('user_comments', models.CharField(max_length=400)),
                ('eid', models.ForeignKey(to='CrowdCon.Event', db_column=b'eid')),
                ('email', models.ForeignKey(to='CrowdCon.Registered_User', db_column=b'email')),
                ('name', models.ForeignKey(to='CrowdCon.Ingredient', db_column=b'name')),
            ],
            options={
                'db_table': 'who_buys',
            },
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='part_of',
            name='email',
            field=models.ForeignKey(to='CrowdCon.Registered_User', db_column=b'email'),
        ),
        migrations.AddField(
            model_name='event_ingredient',
            name='name',
            field=models.ForeignKey(to='CrowdCon.Ingredient', db_column=b'name'),
        ),
    ]
