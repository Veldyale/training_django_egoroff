# Generated by Django 3.2.7 on 2022-02-18 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='', max_length=10),
        ),
    ]
