# Generated by Django 3.2 on 2022-04-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='monthly_expanses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='monthly_income',
            field=models.IntegerField(default=0),
        ),
    ]
