# Generated by Django 3.2.7 on 2022-02-20 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(default=1000000, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1900)]),
        ),
    ]
