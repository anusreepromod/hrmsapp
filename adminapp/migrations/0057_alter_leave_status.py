# Generated by Django 3.2.5 on 2021-12-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0056_remove_leavetype_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
