# Generated by Django 2.2.2 on 2020-04-28 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queuesystem', '0007_queue_system_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queue_system',
            name='doctor',
        ),
    ]
