# Generated by Django 2.2.2 on 2020-04-26 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0006_auto_20200427_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medical_personal',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='picture',
        ),
    ]
