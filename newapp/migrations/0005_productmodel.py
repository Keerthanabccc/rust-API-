# Generated by Django 4.2.6 on 2023-10-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_alter_hotels_rat'),
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50)),
                ('productimg', models.FileField(upload_to='')),
                ('productdis', models.CharField(max_length=50)),
            ],
        ),
    ]
