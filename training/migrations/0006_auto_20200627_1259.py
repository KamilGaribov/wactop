# Generated by Django 3.0.4 on 2020-06-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_auto_20200627_1259'),
        ('training', '0005_auto_20200627_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='training', to='tour.Type', verbose_name='type'),
        ),
    ]
