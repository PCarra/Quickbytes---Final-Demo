# Generated by Django 3.1 on 2020-10-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='item_type',
            field=models.CharField(choices=[('Appetizer', 'Appetizer'), ('Entree', 'Entree'), ('Dessert', 'Dessert'), ('Wine', 'Wine'), ('Beer', 'Beer'), ('Cocktail', 'Cocktail'), ('Side', 'Side')], default='Appetizer', max_length=10),
        ),
    ]
