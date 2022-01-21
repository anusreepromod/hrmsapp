# Generated by Django 3.2.5 on 2021-12-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0050_auto_20211208_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='status',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='designation',
            name='status',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='status',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='status',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='status',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='resignation',
            name='status',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]