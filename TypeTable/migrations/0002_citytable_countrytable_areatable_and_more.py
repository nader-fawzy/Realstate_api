# Generated by Django 5.2 on 2025-05-11 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TypeTable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_en', models.CharField(max_length=100)),
                ('City_ar', models.CharField(max_length=100)),
                ('Status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CountryTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country_en', models.CharField(max_length=100)),
                ('Country_ar', models.CharField(max_length=100)),
                ('Status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AreaTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area_en', models.CharField(max_length=100)),
                ('Area_ar', models.CharField(max_length=100)),
                ('Status', models.BooleanField()),
                ('City_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TypeTable.citytable')),
            ],
        ),
        migrations.AddField(
            model_name='citytable',
            name='Country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TypeTable.countrytable'),
        ),
    ]
