# Generated by Django 3.2.7 on 2022-02-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=1900),
        ),
    ]
