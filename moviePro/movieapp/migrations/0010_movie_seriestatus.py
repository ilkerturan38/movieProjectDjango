# Generated by Django 4.0.4 on 2022-04-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0009_alter_movie_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='serieStatus',
            field=models.BooleanField(default=False, verbose_name='Seri Durumu'),
        ),
    ]