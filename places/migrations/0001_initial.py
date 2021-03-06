# Generated by Django 3.1.7 on 2021-04-09 12:02

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_type', models.CharField(help_text='Enter place type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('type_of_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.placetype')),
            ],
        ),
    ]
