# Generated by Django 3.2.19 on 2023-05-29 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0005_alter_recipe_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image_2',
        ),
    ]