# Generated by Django 3.1.13 on 2021-09-21 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_export', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='export',
            name='only_finished',
        ),
        migrations.RemoveField(
            model_name='export',
            name='task_ids',
        ),
    ]
