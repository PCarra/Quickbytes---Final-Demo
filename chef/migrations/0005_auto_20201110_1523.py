# Generated by Django 3.1 on 2020-11-10 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0004_auto_20201110_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='ingredient',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='supplyorder',
            name='ingredient',
            field=models.ForeignKey(db_column='ingredient', on_delete=django.db.models.deletion.CASCADE, to='chef.ingredients'),
        ),
    ]
