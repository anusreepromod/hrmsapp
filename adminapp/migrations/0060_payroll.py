# Generated by Django 3.2.5 on 2021-12-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0059_allowance'),
    ]

    operations = [
        migrations.CreateModel(
            name='payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic', models.CharField(max_length=40)),
                ('hra', models.CharField(max_length=40)),
                ('specialallowance', models.CharField(max_length=40)),
                ('medicalallowance', models.CharField(max_length=40)),
                ('conveyance', models.CharField(max_length=40)),
                ('grossearning', models.CharField(max_length=40)),
                ('ptax', models.CharField(max_length=40)),
                ('grossdeduction', models.CharField(max_length=40)),
                ('netpay', models.CharField(max_length=40)),
            ],
        ),
    ]