# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('tip_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('canonicalurl', models.CharField(max_length=300, db_column='canonicalUrl', blank=True)),
                ('likes', models.IntegerField(null=True, blank=True)),
                ('likes_content', models.CharField(max_length=2000, blank=True)),
                ('text', models.CharField(max_length=2000, blank=True)),
            ],
            options={
                'db_table': 'tips',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=45, blank=True)),
                ('gender', models.CharField(max_length=45, blank=True)),
                ('photo', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'db_table': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venue_id', models.CharField(max_length=60, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, blank=True)),
                ('location', models.CharField(max_length=1000, blank=True)),
                ('menu', models.CharField(max_length=1000, blank=True)),
                ('stats', models.CharField(max_length=1000, blank=True)),
                ('categories', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'db_table': 'venues',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tip',
            name='user',
            field=models.ForeignKey(blank=True, to='search.User', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tip',
            name='venue',
            field=models.ForeignKey(blank=True, to='search.Venue', null=True),
            preserve_default=True,
        ),
    ]
