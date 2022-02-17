# Generated by Django 3.2.7 on 2022-02-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('rating', models.IntegerField()),
                ('year', models.IntegerField(default=1999)),
                ('budget', models.IntegerField(default=1000000)),
            ],
        ),
    ]
