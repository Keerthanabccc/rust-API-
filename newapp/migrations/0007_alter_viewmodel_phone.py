# Generated by Django 4.2.6 on 2023-10-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_viewmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewmodel',
            name='phone',
            field=models.FloatField(),
        ),
    ]
