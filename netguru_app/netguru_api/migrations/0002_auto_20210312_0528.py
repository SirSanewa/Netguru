# Generated by Django 3.1.7 on 2021-03-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netguru_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='avg_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='car',
            name='rates_number',
            field=models.IntegerField(default=0),
        ),
    ]
