# Generated by Django 4.0.4 on 2022-04-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='movieCategory', to='movieapp.genre', verbose_name='Film Türü'),
        ),
    ]
