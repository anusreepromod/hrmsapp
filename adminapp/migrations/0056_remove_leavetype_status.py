# Generated by Django 3.2.5 on 2021-12-08 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0055_alter_leave_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavetype',
            name='status',
        ),
    ]
