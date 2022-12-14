# Generated by Django 4.1.1 on 2022-09-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0003_remove_article_subtract_remove_article_text_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="article", name="active",),
        migrations.AddField(
            model_name="article",
            name="subtract",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.BooleanField(default=True),
        ),
    ]
