# Generated by Django 3.1.3 on 2021-02-11 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210211_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='cityNameENG',
        ),
        migrations.RemoveField(
            model_name='city',
            name='countryENG',
        ),
    ]
