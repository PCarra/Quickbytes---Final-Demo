# Generated by Django 3.1 on 2020-11-10 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='SupplyOrder',
        ),
    ]
