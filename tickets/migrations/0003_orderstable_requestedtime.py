# Generated by Django 3.1 on 2020-11-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_remove_orderstable_requestedtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstable',
            name='requestedtime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]