# Generated by Django 4.1.1 on 2022-09-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0002_fruit_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='buy',
            field=models.BooleanField(default=False),
        ),
    ]
