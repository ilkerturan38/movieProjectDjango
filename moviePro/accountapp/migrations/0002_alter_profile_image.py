# Generated by Django 4.0.4 on 2022-05-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='Profil Resmi'),
        ),
    ]
