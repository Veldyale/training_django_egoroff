# Generated by Django 3.2.7 on 2022-02-21 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_auto_20220221_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], default='M', max_length=1),
        ),
    ]
