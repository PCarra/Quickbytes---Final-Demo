# Generated by Django 3.1 on 2020-11-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0003_auto_20201110_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
