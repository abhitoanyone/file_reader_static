# Generated by Django 3.2 on 2022-04-16 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220416_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='monthly_expanses',
            new_name='monthly_expenses',
        ),
    ]
