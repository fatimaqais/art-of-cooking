# Generated by Django 3.2.19 on 2023-05-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0003_auto_20230512_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
