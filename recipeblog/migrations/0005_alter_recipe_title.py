# Generated by Django 3.2.19 on 2023-05-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0004_recipe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
