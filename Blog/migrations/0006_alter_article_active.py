# Generated by Django 4.1.1 on 2022-09-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_remove_article_subtract_article_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='active',
            field=models.BooleanField(),
        ),
    ]